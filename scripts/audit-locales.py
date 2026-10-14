#!/usr/bin/env python3
"""Audit every locale against locales/en-001: all pages and files present, every README.md a symlink to index.md,
no stray files, translated slugs, slug hygiene, and every link/anchor resolving.
Run from anywhere: python3 scripts/audit-locales.py (exit status 1 on any problem)."""
import os,re,sys,filecmp,unicodedata,urllib.parse,collections
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','locales'))
SRC='en-001'; SECS=['documents','templates','examples']
def peer(p):
    f=p+'/.locale-peer-id'
    return open(f).read().strip() if os.path.isfile(f) else ''
def tree(root):
    """secpeer -> secdir ; peer -> (secdir, dir)"""
    secs={}; pages={}
    for s in sorted(os.listdir(root)):
        sp=f'{root}/{s}'
        if not os.path.isdir(sp): continue
        sid=peer(sp)
        secs[s]=sid
        for d in sorted(os.listdir(sp)):
            dp=f'{sp}/{d}'
            if os.path.isdir(dp): pages[peer(dp) or ('?',s,d)]=(s,d)
    return secs,pages
esecs,epages=tree(SRC)
enkind={s:peer(f'{SRC}/{s}') for s in SECS}
def files_in(p): return sorted(f for f in os.listdir(p) if os.path.isfile(f'{p}/{f}') or os.path.islink(f'{p}/{f}'))
PRODUCT_OK={'amazon-web-services','google-cloud-platform','microsoft-azure-devops','tailwind-css'}
ENGLISH_VARIANTS={'en-gb','en-us','en-ie'}
# Slugs that are genuinely identical in the language (cognates), reviewed by hand.
COGNATES={'da-001':{'css-framework','mysql-database','postgresql-database','python-django-framework','ruby-on-rails-framework','sveltekit-framework'},
 'nl-001':{'css-framework','mysql-database','postgresql-database','python-django-framework','ruby-on-rails-framework','sveltekit-framework'},
 'de-001':{'css-framework','python-django-framework','ruby-on-rails-framework','sveltekit-framework'},
 'id-001':{'monorepo-vs-multirepo'},'fr-001':{'documents'}}
# A regional copy (nl-nl) shares its -001 locale's cognates.
def cog(loc): return COGNATES.get(loc, COGNATES.get(loc[:2]+'-001', ()))
# Every README.md must be a symlink to the index.md beside it; no other symlinks are allowed.
locs=sorted(x for x in os.listdir('.') if re.match(r'^[a-z]{2,3}-[a-z0-9]{2,3}$',x) and x!=SRC)
for dp,_,fs in os.walk(SRC):
    for f in fs:
        q=f'{dp}/{f}'
        if (f=='README.md') != os.path.islink(q) or (f=='README.md' and os.readlink(q)!='index.md'):
            print('SOURCE README/symlink problem',q); sys.exit(1)
problems=collections.defaultdict(list)
if os.system('python3 ../scripts/build-locale-sitemaps.py --check')!=0: problems['sitemaps'].append('a locale sitemap.xml is stale: run scripts/build-locale-sitemaps.py')
for loc in locs:
    secs,pages=tree(loc)
    # section dirs: map by peer id; examples section has empty id -> match by being the remaining
    kinds={}
    for s,sid in secs.items():
        for k,v in enkind.items():
            if sid and sid==v: kinds[s]=k
    rem=[s for s in secs if s not in kinds]
    if len(rem)==1: kinds[rem[0]]='examples'
    if sorted(kinds.values())!=sorted(SECS): problems[loc].append(f'section dirs not 3: {kinds}')
    if loc not in ENGLISH_VARIANTS:
        for s,k in kinds.items():
            if s==k and s not in cog(loc): problems[loc].append(f'section dir not translated: {s}')
    # root files
    rootfiles=files_in(loc); enroot=files_in(SRC)
    # pages
    for pid,(es,ed) in epages.items():
        if isinstance(pid,tuple): continue
        if pid not in pages: problems[loc].append(f'MISSING page {es}/{ed}'); continue
        ls,ld=pages[pid]
        ep=f'{SRC}/{es}/{ed}'; lp=f'{loc}/{ls}/{ld}'
        # required files
        for f in files_in(ep):
            if f=='.DS_Store': continue
            if not os.path.isfile(f'{lp}/{f}'): problems[loc].append(f'missing file {ls}/{ld}/{f}')
        extra=[f for f in files_in(lp) if f not in files_in(ep) and f!='.DS_Store']
        if extra: problems[loc].append(f'extra files {ls}/{ld}: {extra}')
        # index/readme parity and non-empty
        for f in ('index.md','README.md'):
            q=f'{lp}/{f}'
            if os.path.isfile(q) and os.path.getsize(q)<50: problems[loc].append(f'tiny file {q}')
        if os.path.isfile(lp+'/index.md') and os.path.isfile(lp+'/README.md') and not filecmp.cmp(lp+'/index.md',lp+'/README.md',shallow=False): problems[loc].append(f'index!=README {ls}/{ld}')
        # slug translated?
        if loc not in ENGLISH_VARIANTS and ld==ed and ed not in PRODUCT_OK and ed not in cog(loc): problems[loc].append(f'slug not translated: {ed}')
        if loc not in ENGLISH_VARIANTS and ld==ed and ed in PRODUCT_OK: problems[loc].append(f'(product-name slug kept) {ed}')
        # slug hygiene
        if re.search(r'[\sA-Z_.]',ld) and not re.search(r'[一-鿿]',ld): problems[loc].append(f'slug hygiene: {ld}')
        if re.search(r'\s',ld): problems[loc].append(f'slug has space: {ld}')
        # does the slug contain any letters of the locale's script (non-ASCII) or at least differ
    # section-level files
    for s,k in kinds.items():
        for f in ('index.md','README.md'):
            ex=os.path.isfile(f'{SRC}/{k}/{f}'); lo=os.path.isfile(f'{loc}/{s}/{f}')
            if ex!=lo: problems[loc].append(f'section {f} presence {k}: en={ex} loc={lo}')
        if os.path.isfile(f'{loc}/{s}/index.md') and os.path.isfile(f'{loc}/{s}/README.md') and not filecmp.cmp(f'{loc}/{s}/index.md',f'{loc}/{s}/README.md',shallow=False): problems[loc].append(f'section index!=README {s}')
    # stray
    for dp,dn,fn in os.walk(loc):
        for f in fn:
            if f=='.DS_Store': problems[loc].append(f'stray {dp}/{f}')
            q=f'{dp}/{f}'
            if f=='README.md':
                if not os.path.islink(q) or os.readlink(q)!='index.md': problems[loc].append(f'README.md must be a symlink to index.md: {q}')
            elif os.path.islink(q): problems[loc].append(f'unexpected symlink {q}')
    # root index.md = the translated README: 15 sections, README.md symlink beside it
    root_ok=os.path.isfile(f'{loc}/index.md')
    if root_ok:
        if not os.path.islink(f'{loc}/README.md'): problems[loc].append('root README.md must be a symlink to index.md')
        nh=0;fence=False
        for l in open(f'{loc}/index.md',encoding='utf8'):
            if l.startswith('```'): fence=not fence
            if not fence and l.startswith('## '): nh+=1
        if nh!=15: problems[loc].append(f'root index.md has {nh} sections, expected 15')
    else: problems[loc].append('missing root index.md (translated README)')
    allf=sum(len([f for f in fs if f!='sitemap.xml']) for _,_,fs in os.walk(loc))
    if not os.path.isfile(f'{loc}/sitemap.xml'): problems[loc].append('missing sitemap.xml (run scripts/build-locale-sitemaps.py)')
    want=205 if root_ok else 203
    if allf!=want: problems[loc].append(f'file count {allf} != {want}')
for loc in locs:
    pr=problems.get(loc,[])
    real=[p for p in pr if not p.startswith('(product')]
    print(f"{loc}: {'OK' if not real else str(len(real))+' problem(s)'}"+(f"  [{len([p for p in pr if p.startswith('(product')])} product-name slugs kept]" if any(p.startswith('(product') for p in pr) else ''))
    for p in real[:12]: print('    ',p)

# ---- links and anchors (every relative link and #fragment must resolve) ----
def slug(h):
    h=h.strip().lower()
    return ''.join(c for c in h if unicodedata.category(c)[0] in 'LMN' or c in '-_ ').replace(' ','-')
_cache={}
def anchors(p):
    if p in _cache: return _cache[p]
    seen={};out=set();fence=False
    for l in open(p,encoding='utf8'):
        if l.startswith('```'): fence=not fence
        if fence: continue
        m=re.match(r'#{1,6}\s+(.*)',l)
        if m:
            s=slug(re.sub(r'[`*]','',m.group(1)))
            if s in seen: seen[s]+=1; s=f"{s}-{seen[s]}"
            else: seen[s]=0
            out.add(s)
    _cache[p]=out; return out
nlinks=nanch=0
for root in [SRC]+locs:
    for dp,_,fs in os.walk(root):
        for f in fs:
            if not f.endswith('.md'): continue
            p=os.path.join(dp,f); t=open(p,encoding='utf8').read()
            for m in re.finditer(r'\]\(([^)\s]+)\)',t):
                u=m.group(1)
                if re.match(r'(https?:|mailto:)',u) or u=='0005-example.md': continue   # 0005-example.md: MADR placeholder
                path,_,frag=u.partition('#'); path=urllib.parse.unquote(path)
                tgt=p if not path else os.path.normpath(os.path.join(dp,path))
                if path and os.path.isdir(tgt): tgt=os.path.join(tgt,'index.md')
                if not os.path.exists(tgt): nlinks+=1; print('BROKEN LINK',p,u); continue
                if frag and tgt.endswith('.md') and urllib.parse.unquote(frag).lower() not in anchors(tgt): nanch+=1; print('BAD ANCHOR',p,u)
print(f"links: {nlinks} broken, anchors: {nanch} bad")
real=[(l,p) for l in locs for p in problems.get(l,[]) if not p.startswith('(product')]
print('unresolved problems:',len(real))
if nlinks or nanch or real: sys.exit(1)
