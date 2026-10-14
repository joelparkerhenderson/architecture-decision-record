# บันทึกการตัดสินใจด้านสถาปัตยกรรม (ADR)

บันทึกการตัดสินใจด้านสถาปัตยกรรม (ADR) คือเอกสารที่บันทึกการตัดสินใจด้านสถาปัตยกรรมที่สำคัญ พร้อมบริบทและผลที่ตามมา

> [!IMPORTANT]
> โปรดตรวจสอบทรัพยากรเหล่านี้ด้วยตนเองอย่างรอบคอบก่อนนำไปใช้ในระบบที่สำคัญ

สารบัญ:

- [บันทึกการตัดสินใจด้านสถาปัตยกรรมคืออะไร](#บันทึกการตัดสินใจด้านสถาปัตยกรรมคืออะไร)
- [วิธีเริ่มต้นใช้ ADR](#วิธีเริ่มต้นใช้-adr)
- [วิธีเริ่มต้นใช้ ADR ด้วยเครื่องมือ](#วิธีเริ่มต้นใช้-adr-ด้วยเครื่องมือ)
- [วิธีเริ่มต้นใช้ ADR ด้วย git](#วิธีเริ่มต้นใช้-adr-ด้วย-git)
- [สกิล Claude Code สำหรับ ADR](#สกิล-claude-code-สำหรับ-adr)
- [แนวปฏิบัติในการตั้งชื่อไฟล์](#แนวปฏิบัติในการตั้งชื่อไฟล์)
- [ข้อเสนอแนะในการเขียน ADR ที่ดี](#ข้อเสนอแนะในการเขียน-adr-ที่ดี)
- [แม่แบบตัวอย่าง ADR](#แม่แบบตัวอย่าง-adr)
- [คำแนะนำด้านการทำงานเป็นทีมสำหรับ ADR](#คำแนะนำด้านการทำงานเป็นทีมสำหรับ-adr)
- [คำถามเรื่องการทำงานเป็นทีมสำหรับ ADR](#คำถามเรื่องการทำงานเป็นทีมสำหรับ-adr)
- [แนวคิดขั้นต่อไปสำหรับ ADR](#แนวคิดขั้นต่อไปสำหรับ-adr)
- [แผนภาพ มุมมอง และมุมมองเชิงสถาปัตยกรรม](#แผนภาพ-มุมมอง-และมุมมองเชิงสถาปัตยกรรม)
- [ฟังก์ชันความเหมาะสมสำหรับการตัดสินใจในรูปแบบโค้ด](#ฟังก์ชันความเหมาะสมสำหรับการตัดสินใจในรูปแบบโค้ด)
- [ราวกั้นการตัดสินใจสำหรับ pull request](#ราวกั้นการตัดสินใจสำหรับ-pull-request)
- [ข้อมูลเพิ่มเติม](#ข้อมูลเพิ่มเติม)

แม่แบบ:

- [แม่แบบบันทึกการตัดสินใจโดย Jeff Tyree และ Art Akerman](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-jeff-tyree-และ-art-akerman/)
- [แม่แบบบันทึกการตัดสินใจโดย Michael Nygard](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-michael-nygard/)
- [แม่แบบบันทึกการตัดสินใจโดย EdgeX](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-edgex/)
- [แม่แบบบันทึกการตัดสินใจโดย arc42](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-arc42/)
- [แม่แบบบันทึกการตัดสินใจสำหรับรูปแบบอเล็กซานเดรีย](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับรูปแบบอเล็กซานเดรีย/)
- [แม่แบบบันทึกการตัดสินใจสำหรับกรณีทางธุรกิจ](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับกรณีทางธุรกิจ/)
- [แม่แบบบันทึกการตัดสินใจของโครงการ MADR](แม่แบบ/แม่แบบบันทึกการตัดสินใจของโครงการ-madr/)
- [แม่แบบบันทึกการตัดสินใจด้วย Planguage](แม่แบบ/แม่แบบบันทึกการตัดสินใจด้วย-planguage/)
- [แม่แบบบันทึกการตัดสินใจโดย Paulo Merson](https://github.com/pmerson/ADR-template)
- [แม่แบบบันทึกการตัดสินใจโดย Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [แม่แบบบันทึกการตัดสินใจโดย Gareth Morgan](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-gareth-morgan/)
- [แม่แบบบันทึกการตัดสินใจโดย GIG Cymru NHS Wales](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-gig-cymru-nhs-wales/)
- [แม่แบบบันทึกการตัดสินใจสำหรับการตัดสินใจทางเทคนิคที่สำคัญ (ITD) โดย Ignacio Larrañaga](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับการตัดสินใจทางเทคนิคที่สำคัญ/)

ตัวอย่าง:

- [เฟรมเวิร์ก CSS](ตัวอย่าง/เฟรมเวิร์ก-css/)
- [การกำหนดค่าด้วยตัวแปรสภาพแวดล้อม](ตัวอย่าง/การกำหนดค่าด้วยตัวแปรสภาพแวดล้อม/)
- [เมตริก การเฝ้าติดตาม การแจ้งเตือน](ตัวอย่าง/เมตริก-การเฝ้าติดตาม-การแจ้งเตือน/)
- [Microsoft Azure DevOps](ตัวอย่าง/microsoft-azure-devops/)
- [Monorepo หรือ multirepo](ตัวอย่าง/monorepo-หรือ-multirepo/)
- [ภาษาโปรแกรม](ตัวอย่าง/ภาษาโปรแกรม/)
- [การจัดเก็บความลับ](ตัวอย่าง/การจัดเก็บความลับ/)
- [รูปแบบการประทับเวลา](ตัวอย่าง/รูปแบบการประทับเวลา/)
- [และอีกมากมาย...](ตัวอย่าง/)

## บันทึกการตัดสินใจด้านสถาปัตยกรรมคืออะไร

**บันทึกการตัดสินใจด้านสถาปัตยกรรม** (ADR) คือเอกสารที่บันทึกการตัดสินใจด้านสถาปัตยกรรมที่สำคัญซึ่งได้ทำไปแล้ว พร้อมบริบทและผลที่ตามมา

**การตัดสินใจด้านสถาปัตยกรรม** (AD) คือทางเลือกในการออกแบบซอฟต์แวร์ที่ตอบสนองข้อกำหนดที่มีนัยสำคัญ

**บันทึกการตัดสินใจด้านสถาปัตยกรรม** (ADL) คือชุดของ ADR ทั้งหมดที่สร้างและดูแลสำหรับโครงการ (หรือองค์กร) หนึ่ง

**ข้อกำหนดที่มีนัยสำคัญด้านสถาปัตยกรรม** (ASR) คือข้อกำหนดที่มีผลที่วัดได้ต่อสถาปัตยกรรมของระบบซอฟต์แวร์

ทั้งหมดนี้อยู่ภายใต้หัวข้อ **การจัดการความรู้ด้านสถาปัตยกรรม** (AKM)

เป้าหมายของเอกสารนี้คือให้ภาพรวมโดยย่อเกี่ยวกับ ADR วิธีเขียน และที่ที่จะหาข้อมูลเพิ่มเติม

ตัวย่อ:

  * **AD**: การตัดสินใจด้านสถาปัตยกรรม

  * **ADL**: บันทึกการตัดสินใจด้านสถาปัตยกรรม

  * **ADR**: บันทึกการตัดสินใจด้านสถาปัตยกรรม

  * **AKM**: การจัดการความรู้ด้านสถาปัตยกรรม

  * **ASR**: ข้อกำหนดที่มีนัยสำคัญด้านสถาปัตยกรรม

## วิธีเริ่มต้นใช้ ADR

เพื่อเริ่มต้นใช้ ADR ให้พูดคุยกับเพื่อนร่วมทีมเกี่ยวกับด้านต่อไปนี้

การระบุการตัดสินใจ:

  * AD เร่งด่วนและสำคัญเพียงใด

  * ต้องตัดสินใจตอนนี้ หรือรอจนกว่าจะรู้มากขึ้นได้

  * ประสบการณ์ส่วนตัวและส่วนรวม รวมถึงวิธีการและแนวปฏิบัติด้านการออกแบบที่เป็นที่ยอมรับ ช่วยระบุการตัดสินใจได้

  * ในอุดมคติ ให้มีรายการงานค้าง (backlog) ของการตัดสินใจที่เสริมรายการงานค้างของผลิตภัณฑ์

การตัดสินใจ:

  * มีเทคนิคหลายอย่างสำหรับการตัดสินใจ ทั้งเทคนิคทั่วไปและเทคนิคเฉพาะสถาปัตยกรรมซอฟต์แวร์ ตัวอย่างหนึ่งคือ dialogue mapping

  * การตัดสินใจเป็นกลุ่มเป็นหัวข้อวิจัยที่ยังคึกคัก

การบังคับใช้และการดำเนินการตามการตัดสินใจ:

  * เนื่องจาก AD ใช้ในการออกแบบซอฟต์แวร์ จึงต้องสื่อสารไปยังผู้มีส่วนได้ส่วนเสียที่สนับสนุนเงินทุน พัฒนา และดำเนินงานระบบ และต้องได้รับการยอมรับจากพวกเขา

  * รูปแบบการเขียนโค้ดที่คำนึงถึงสถาปัตยกรรมและการทบทวนโค้ดที่เน้นประเด็นและการตัดสินใจด้านสถาปัตยกรรมเป็นสองแนวปฏิบัติที่เกี่ยวข้อง

  * ควรพิจารณา AD (ใหม่) เมื่อปรับปรุงระบบซอฟต์แวร์ให้ทันสมัยระหว่างวิวัฒนาการของซอฟต์แวร์ด้วย

การแบ่งปันการตัดสินใจ (ทางเลือก):

  * AD จำนวนมากเกิดซ้ำข้ามโครงการ

  * ดังนั้น ประสบการณ์จากการตัดสินใจในอดีต ทั้งดีและไม่ดี อาจเป็นทรัพย์สินที่นำกลับมาใช้ซ้ำได้อย่างมีค่าเมื่อใช้กลยุทธ์การจัดการความรู้ที่ชัดเจน

การบันทึกการตัดสินใจ:

  * มีแม่แบบและเครื่องมือมากมายสำหรับบันทึกการตัดสินใจ

  * ดูชุมชน agile เช่น ADR ของ M. Nygard

  * ดูกระบวนการวิศวกรรมซอฟต์แวร์และการออกแบบสถาปัตยกรรมแบบดั้งเดิม เช่น IBM UMF และรูปแบบตารางที่ Tyree และ Akerman จาก CapitalOne เสนอ

อ่านเพิ่มเติม:

  * ขั้นตอนข้างต้นนำมาจากบทความ Wikipedia [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## วิธีเริ่มต้นใช้ ADR ด้วยเครื่องมือ

- [MySpec](https://myspec.dev) — แพลตฟอร์มข้อกำหนดและการตัดสินใจด้านสถาปัตยกรรมอัตโนมัติ ที่จัดโครงสร้างกฎบัตรโครงการ สถาปัตยกรรมเชิงเทคนิค และ ADR ให้เป็น Markdown ที่สะอาด และให้บริการผ่าน MCP

คุณเลือกได้เองว่าจะเริ่มต้นใช้ ADR ด้วยเครื่องมืออย่างไร

ตัวอย่างเช่น:

  * หากคุณชอบ Google Drive และการแก้ไขออนไลน์ คุณสร้างเอกสาร Google หรือสเปรดชีต Google ได้

  * หากคุณชอบระบบควบคุมเวอร์ชันซอร์สโค้ดอย่าง git คุณสร้างไฟล์สำหรับแต่ละ ADR ได้

  * หากคุณชอบเครื่องมือวางแผนโครงการอย่าง Atlassian Jira คุณใช้ตัวติดตามการวางแผนของเครื่องมือนั้นได้

  * หากคุณชอบวิกิอย่าง MediaWiki คุณสร้างวิกิ ADR ได้

## วิธีเริ่มต้นใช้ ADR ด้วย git

หากคุณชอบระบบควบคุมเวอร์ชัน git นี่คือวิธีที่เราเริ่มต้นใช้ ADR ด้วย git ในโครงการซอฟต์แวร์ทั่วไปที่มีซอร์สโค้ด

สร้างไดเรกทอรีสำหรับไฟล์ ADR ของคุณ:

```sh
$ mkdir adr
```

สำหรับแต่ละ ADR สร้างไฟล์ข้อความ เช่น `database.txt`:

```sh
$ vi database.txt
```

เขียนอะไรก็ได้ที่คุณต้องการใน ADR ดูแม่แบบในที่เก็บนี้เพื่อหาแนวคิด

commit ADR ไปยังที่เก็บ git ของคุณ

## สกิล Claude Code สำหรับ ADR

คลังนี้มาพร้อมสกิล [Claude Code](https://claude.com/claude-code) สองรายการใน [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) เพื่อให้เอเจนต์เขียนโค้ดด้วย AI เขียนและดูแล ADR ตามแนวทางที่โครงการนี้แนะนำ:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ใช้งานทั่วไป สำหรับทุกคนที่เขียน ADR ในโครงการใดก็ได้ ช่วยตัดสินใจว่าการตัดสินใจนั้นต้องมี ADR หรือไม่ สร้างไดเรกทอรี `adr/` หรือ `decisions/` ตั้งชื่อไฟล์ เลือกแม่แบบจากโครงร่างสิบเอ็ดแบบที่มาให้ และเขียนส่วนบริบท/การตัดสินใจ/ผลที่ตามมาได้อย่างหนักแน่น

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — สำหรับผู้ดูแลคลังนี้โดยเฉพาะ บันทึกโครงสร้างของคลัง แนวปฏิบัติในการทำให้ README และ locales ตรงกัน และขั้นตอนที่แน่ชัดในการเพิ่มแม่แบบ ตัวอย่าง หรือลิงก์เครื่องมือใหม่

หากต้องการใช้สกิล ให้คัดลอกโฟลเดอร์ของสกิลไปไว้ที่ `.claude/skills/` ที่รากของคลังที่คุณทำงานอยู่ (หรือไปที่ `~/.claude/skills/` เพื่อให้ใช้ได้ในทุกโครงการ) จากนั้นขอให้ Claude Code เขียนหรือทบทวน ADR

## แนวปฏิบัติในการตั้งชื่อไฟล์

หากคุณเลือกเขียน ADR เป็นไฟล์ข้อความธรรมดา อาจเป็นประโยชน์ที่จะกำหนดแนวปฏิบัติในการตั้งชื่อไฟล์ ADR ของคุณเอง

เราชอบแนวปฏิบัติในการตั้งชื่อไฟล์ที่มีรูปแบบเฉพาะ

ตัวอย่าง:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

แนวปฏิบัติในการตั้งชื่อไฟล์ของเรา:

  * ชื่อเป็นวลีกริยาแบบคำสั่งในกาลปัจจุบัน ซึ่งช่วยให้อ่านง่ายขึ้นและตรงกับรูปแบบข้อความ commit ของเรา

  * ชื่อใช้ตัวพิมพ์เล็กและเครื่องหมายขีดกลาง (เหมือนในที่เก็บนี้) นี่คือความสมดุลระหว่างความอ่านง่ายและการใช้งานข้ามระบบ

  * นามสกุลคือ markdown ซึ่งอาจสะดวกสำหรับการจัดรูปแบบอย่างง่าย

## ข้อเสนอแนะในการเขียน ADR ที่ดี

ลักษณะของ ADR ที่ดี:

* เหตุผล: อธิบายว่าทำไมจึงดำเนิน AD ซึ่งอาจรวมถึงบริบท (ดูด้านล่าง) ข้อดีข้อเสียของทางเลือกที่เป็นไปได้ต่าง ๆ การเปรียบเทียบฟีเจอร์ การอภิปรายต้นทุนและผลประโยชน์ และอื่น ๆ

* เฉพาะเจาะจง: แต่ละ ADR ควรเกี่ยวกับ AD หนึ่งรายการ ไม่ใช่หลาย AD

* มีการประทับเวลา: ระบุว่ารายการแต่ละรายการใน ADR เขียนเมื่อใด ซึ่งสำคัญเป็นพิเศษสำหรับแง่มุมที่อาจเปลี่ยนไปตามเวลา เช่น ต้นทุน กำหนดการ การขยาย และอื่น ๆ

* แก้ไขไม่ได้: อย่าเปลี่ยนข้อมูลที่มีอยู่ใน ADR ให้แก้ไข ADR โดยเพิ่มข้อมูลใหม่แทน หรือแทนที่ ADR ด้วยการสร้าง ADR ใหม่

ลักษณะของส่วน "บริบท" ที่ดีใน ADR:

* อธิบายสถานการณ์ขององค์กรและลำดับความสำคัญทางธุรกิจ

* รวมเหตุผลและข้อพิจารณาที่อิงจากองค์ประกอบทางสังคมและทางเทคนิคของทีม

* รวมข้อแลกเปลี่ยนที่เกี่ยวข้อง แสดงในคำที่ตรงกับความต้องการและเป้าหมาย

ลักษณะของส่วน "ผลที่ตามมา" ที่ดีใน ADR:

* อธิบายสิ่งที่ตามมาจากการตัดสินใจ ซึ่งอาจรวมถึงผลกระทบ ผลลัพธ์ ผลงานส่งมอบ การดำเนินการติดตามผล และอื่น ๆ

* รวมข้อมูลเกี่ยวกับ ADR ที่ตามมา เป็นเรื่องที่พบได้ค่อนข้างบ่อยที่ ADR หนึ่งทำให้เกิดความจำเป็นต้องมี ADR เพิ่มเติม เช่น เมื่อ ADR หนึ่งเลือกทางเลือกใหญ่ครอบคลุม ก็อาจก่อให้เกิดความจำเป็นต้องมีการตัดสินใจย่อยลงมา

* รวมกระบวนการทบทวนย้อนหลัง เป็นเรื่องปกติที่ทีมจะทบทวนแต่ละ ADR หลังหนึ่งเดือน เปรียบเทียบข้อมูล ADR กับสิ่งที่เกิดขึ้นจริง แล้วเรียนรู้และเติบโตจากสิ่งนั้น

ADR ใหม่อาจแทนที่ ADR ก่อนหน้า:

* เมื่อมีการทำ AD ที่แทนที่หรือทำให้ ADR ก่อนหน้าเป็นโมฆะ ควรเขียน ADR ใหม่

## แม่แบบตัวอย่าง ADR

แม่แบบตัวอย่าง ADR ที่เรารวบรวมไว้จากอินเทอร์เน็ต:

- [แม่แบบ ADR โดย Michael Nygard](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-michael-nygard/) (เรียบง่ายและเป็นที่นิยม)

- [แม่แบบ ADR โดย Jeff Tyree และ Art Akerman](แม่แบบ/แม่แบบบันทึกการตัดสินใจโดย-jeff-tyree-และ-art-akerman/) (ซับซ้อนกว่า)

- [แม่แบบ ADR สำหรับรูปแบบ Alexandrian](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับรูปแบบอเล็กซานเดรีย/) (เรียบง่าย พร้อมรายละเอียดของบริบท)

- [แม่แบบ ADR สำหรับกรณีทางธุรกิจ](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับกรณีทางธุรกิจ/) (เน้นมุมมอง MBA มากกว่า มีต้นทุน SWOT และความเห็นเพิ่มเติม)

- [แม่แบบ ADR ของโครงการ Markdown Any Decision Records (MADR)](แม่แบบ/แม่แบบบันทึกการตัดสินใจของโครงการ-madr/) (มีทั้งฉบับเรียบง่ายและฉบับละเอียด ฉบับหลังเน้นตัวเลือกและข้อดีข้อเสีย)

- [แม่แบบ ADR ที่ใช้ Planguage](แม่แบบ/แม่แบบบันทึกการตัดสินใจด้วย-planguage/) (เน้นการประกันคุณภาพมากกว่า)

- [แม่แบบสำหรับการตัดสินใจทางเทคนิคที่สำคัญ (ITD) โดย Ignacio Larrañaga](แม่แบบ/แม่แบบบันทึกการตัดสินใจสำหรับการตัดสินใจทางเทคนิคที่สำคัญ/) (กระชับและให้การตัดสินใจมาก่อน ปรับให้เหมาะกับการทบทวนอย่างรวดเร็วของผู้บริหาร)

## คำแนะนำด้านการทำงานเป็นทีมสำหรับ ADR

หากคุณกำลังพิจารณาใช้บันทึกการตัดสินใจในทีมของคุณ นี่คือคำแนะนำที่เราเรียนรู้จากการทำงานกับหลายทีม

มีโอกาสที่จะนำสมาชิกทีมด้วยการพูดถึง "ทำไม" แทนที่จะบังคับ "อะไร" ตัวอย่างเช่น บันทึกการตัดสินใจเป็นวิธีที่ทีมจะคิดอย่างชาญฉลาดขึ้นและสื่อสารได้ดีขึ้น หากบันทึกการตัดสินใจเป็นเพียงข้อกำหนดด้านเอกสารที่บังคับทำย้อนหลัง ก็ไม่มีคุณค่า

บางทีมชอบชื่อ "การตัดสินใจ" มากกว่าตัวย่อ "ADR" อย่างมาก เมื่อบางทีมใช้ "decisions" เป็นชื่อไดเรกทอรี ก็เหมือนหลอดไฟสว่างขึ้น และทีมเริ่มใส่ข้อมูลเพิ่มเติมในไดเรกทอรี เช่น การตัดสินใจเกี่ยวกับผู้ขาย การตัดสินใจเกี่ยวกับแผน การตัดสินใจเกี่ยวกับกำหนดการ และอื่น ๆ คุณใช้แม่แบบเดียวกันสำหรับข้อมูลทุกประเภทเหล่านี้ได้ เราสันนิษฐานว่าผู้คนเรียนรู้ได้เร็วกว่าด้วยคำ ("การตัดสินใจ") มากกว่าตัวย่อ ("ADR") ว่าการละคำว่า "บันทึก" ให้แรงจูงใจมากขึ้นในการเขียนงานที่ยังทำอยู่ และว่านักพัฒนาและผู้จัดการบางคนไม่ชอบคำว่า "สถาปัตยกรรม"

ในทางทฤษฎี การแก้ไขไม่ได้เป็นอุดมคติ ในทางปฏิบัติ การแก้ไขได้ทำงานได้ดีกว่าสำหรับทีมของเรา เราแทรกข้อมูลใหม่ลงใน ADR ที่มีอยู่พร้อมตราวันที่และหมายเหตุว่าข้อมูลนั้นมาหลังการตัดสินใจ แนวทางนี้นำไปสู่ "เอกสารที่มีชีวิต" ที่เราทุกคนอัปเดตได้ การอัปเดตทั่วไปมาจากการได้ข้อมูลเพราะสมาชิกทีมใหม่ ข้อเสนอใหม่ ผลจริงจากการใช้งานของเรา หรือหลังการเปลี่ยนแปลงของบุคคลภายนอกในภายหลัง เช่น ฟีเจอร์ของผู้ขาย แผนราคา และสัญญาอนุญาตใช้สิทธิ

## คำถามเรื่องการทำงานเป็นทีมสำหรับ ADR

### ใครเขียน ADR ได้บ้าง

พิจารณาด้านต่าง ๆ เช่น บุคคลเฉพาะ บทบาทเฉพาะ ทีมเฉพาะ แผนกเฉพาะ และพิจารณาด้วยว่ามีบุคคล บทบาท ทีม หรือแผนกที่สามารถว่าจ้างให้เขียน ADR ได้หรือไม่ กล่าวคือขอให้คนอื่นเขียน ADR ได้ 

ตัวอย่างคำตอบ: ทุกคนในองค์กรของเราที่ได้อ่านหน้า README เกี่ยวกับบันทึกการตัดสินใจด้านสถาปัตยกรรมสามารถเสนอ ADR ได้ กล่าวคือเริ่มเขียนและแชร์กับทีม

### อะไรเป็นเหตุผลให้เปิด ADR

พิจารณาด้านต่าง ๆ เช่น วิธีที่ทีมในองค์กรทำงาน โครงสร้างของระบบซอฟต์แวร์ การประสานงานระหว่างทีม ความสามารถในการบำรุงรักษาระยะยาว อินเทอร์เฟซภายนอก และผู้ที่คุณต้องการให้ได้ประโยชน์ 

ตัวอย่างคำตอบ: เราต้องการเขียน ADR เมื่อเราต้องการให้นักพัฒนาในอนาคตเข้าใจ "ทำไม" ของสิ่งที่เราทำ

### อะไรที่ไม่เป็นเหตุผลให้เปิด ADR

พิจารณาด้านต่าง ๆ เช่น การตัดสินใจที่ไม่เกี่ยวกับสถาปัตยกรรม การตัดสินใจที่ไม่สำคัญเพราะความเสี่ยงน้อยที่สุด เป็นอิสระ หรือจำกัดอยู่ที่นักพัฒนาคนเดียว การตัดสินใจที่ได้รับการครอบคลุมอย่างครบถ้วนที่อื่นแล้วในมาตรฐาน นโยบาย เอกสาร และอื่น ๆ หรือการตัดสินใจที่เป็นชั่วคราว เช่น วิธีแก้ขัด การพิสูจน์แนวคิด และการทดลอง 

ตัวอย่างคำตอบ: เราต้องการข้าม ADR เมื่อการตัดสินใจจำกัดในขอบเขต เวลา ความเสี่ยง และต้นทุน หรือมีการครอบคลุมที่อื่นแล้ว

### วงจรชีวิตของ ADR คืออะไร

พิจารณาด้านต่าง ๆ เช่น กระบวนการเขียน กระบวนการค้นคว้า กระบวนการตัดสินใจ กระบวนการนำไปใช้ และกระบวนการยุติการใช้งาน พิจารณาว่าคุณติดตามวงจรชีวิตของ ADR เมื่อเวลาผ่านไปอย่างไร เช่น วิธีเลื่อน ADR จากสถานะหนึ่งไปสถานะถัดไป และวิธีสื่อสารให้ผู้มีส่วนได้ส่วนเสียทราบ 

ตัวอย่างคำตอบ: เราต้องการให้ ADR มีห้าขั้นตอนของวงจรชีวิต: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting

### เกณฑ์สำหรับขั้นตอนวงจรชีวิตของ ADR คืออะไร

พิจารณาด้านต่าง ๆ เช่น เกณฑ์การยอมรับ ADR กล่าวคือเรารู้ได้อย่างไรว่า ADR ดีพอที่จะเลื่อนจากขั้นตอนวงจรชีวิตหนึ่งไปขั้นตอนถัดไป ปัญหาระบุไว้อย่างชัดเจนหรือไม่ ได้พิจารณาทางเลือกอื่นหรือไม่ เข้าใจและบันทึกข้อแลกเปลี่ยนไว้ดีหรือไม่
มีบริบทที่เกี่ยวข้องทั้งหมดหรือไม่ ผู้มีส่วนได้ส่วนเสียที่เกี่ยวข้องทั้งหมดมีส่วนร่วมหรือไม่ นำข้อเสนอแนะทั้งหมดมาปรับใช้แล้วหรือไม่ 

ตัวอย่างคำตอบ: เราต้องการให้ทีมที่ทำงานอยู่ 1) ค้นคว้าให้เสร็จ 2) ประเมินให้เสร็จ 3) เผยแพร่ข้อเสนอ ADR ให้ผู้มีส่วนได้ส่วนเสียพร้อมคำขอความเห็นและกรอบเวลาหนึ่งสัปดาห์ และ 4) เมื่อความเห็นของผู้มีส่วนได้ส่วนเสียทั้งหมดได้รับการนำมาปรับใช้และจัดการแล้ว ให้ผู้มีส่วนได้ส่วนเสียลงคะแนนเกี่ยวกับ ADR

### บทบาทและความรับผิดชอบใดที่เกี่ยวข้องกับ ADR

พิจารณาบทบาทเช่น ผู้ส่ง ผู้ค้นคว้า ผู้ประเมิน ผู้ทบทวน ผู้อนุมัติ และผู้ดูแลรักษา พิจารณาความรับผิดชอบ เช่น การสื่อสารกับผู้มีส่วนได้ส่วนเสีย การทำให้แน่ใจว่าความคาดหวังได้รับการตอบสนอง การแบ่งปันบนเว็บไซต์หรืออินทราเน็ต และการทบทวนงานเป็นระยะ โดยเฉพาะเมื่อมีการเปลี่ยนแปลงที่เกี่ยวข้อง

ตัวอย่างคำตอบ: เราต้องการให้ทุก ADR มีเจ้าของหลัก เจ้าของรอง และทีมที่รับผิดชอบเสมอ พวกเขารับผิดชอบการสื่อสาร การเผยแพร่ การบำรุงรักษา การทบทวนเป็นระยะอย่างน้อยปีละครั้ง และการยุติการใช้งานในท้ายที่สุดเมื่อจำเป็น

### ธรรมาภิบาลเกี่ยวข้องกับ ADR อย่างไร

พิจารณาด้านต่าง ๆ เช่น วิธีที่องค์กรทำงาน ความต้องการด้านการปฏิบัติตามกฎระเบียบเป็นพิเศษ เช่น แง่มุมทางกฎหมายหรือทรัพยากรบุคคล และวิธีที่คุณต้องการจัดการฉันทามติเทียบกับความขัดแย้งเทียบกับการยกระดับ มีด้าน บุคคล หรือทีมใดที่อาจมีอิทธิพลมากกว่าผู้อื่นหรือไม่ เช่น อำนาจในการอนุมัติ ลงคะแนน หรือยับยั้งที่เกี่ยวกับ ADR

ตัวอย่างคำตอบ: ธรรมาภิบาลของ ADR เป็นไปตามลำดับความสำคัญนี้: CEO, CTO, CLO, ทีมที่นำ ADR ไปใช้, ผู้เชี่ยวชาญที่รู้มากที่สุดในทีมเกี่ยวกับ ADD ไม่มีใครมีธรรมาภิบาล เว้นแต่อธิบายไว้ใน ADR 

### หลักการใดที่เกี่ยวข้องกับ ADR

พิจารณาด้านที่เกี่ยวข้องกับวิธีที่องค์กรทำงาน เช่น การเคลื่อนไหวเร็วหรือช้า ฉันทามติของการตัดสินใจเทียบกับความขัดแย้งของการตัดสินใจ ความชอบเสี่ยงเทียบกับความชอบปลอดภัย และการอภิปรายสาธารณะเทียบกับการอภิปรายส่วนตัว

ตัวอย่างคำตอบ: เราใช้หลักการความเป็นผู้นำ ได้แก่ มุ่งเน้นการลงมือทำ (bias for action) เห็นต่างแต่ยึดมั่นร่วมกัน (disagree-and-commit) ข้อมูล 70% เพียงพอสำหรับการตัดสินใจที่ย้อนกลับได้ง่ายและแยกออกได้ง่าย และการทำงานอย่างเปิดเผย ยกเว้นข้อมูลที่เป็นความลับตามที่อธิบายไว้ในข้อตกลงรักษาความลับขององค์กรของเรา

## แนวคิดขั้นต่อไปสำหรับ ADR

[Arc42](https://arc42.org/) ตอบคำถามสองข้อได้อย่างเป็นรูปธรรมและปรับให้เข้ากับความต้องการเฉพาะของคุณได้ คุณควรบันทึก/สื่อสารอะไรเกี่ยวกับสถาปัตยกรรมของคุณ และควรบันทึก/สื่อสารอย่างไร Arc42 รวมบันทึกการตัดสินใจด้านสถาปัตยกรรมพร้อมแนวทางเกี่ยวกับเป้าหมาย ข้อจำกัด บริบท คุณภาพ ความเสี่ยง และอื่น ๆ

[โมเดล C4](https://c4model.com/) เป็นแนวทางวาดแผนภาพสถาปัตยกรรมซอฟต์แวร์ที่เรียนรู้ง่ายและเป็นมิตรกับนักพัฒนา C4 คือชุดแผนภาพลำดับชั้นสำหรับบริบท คอนเทนเนอร์ คอมโพเนนต์ และโค้ด พร้อมแผนภาพสนับสนุนสำหรับภาพรวมของระบบ พลวัต และการปรับใช้

## แผนภาพ มุมมอง และมุมมองเชิงสถาปัตยกรรม

แผนภาพสถาปัตยกรรมเรียกว่า "มุมมองสถาปัตยกรรม"

"มุมมองสถาปัตยกรรม" เป็นตัวอย่างหนึ่งของ "จุดมองสถาปัตยกรรม"

"จุดมองสถาปัตยกรรม" คำนึงถึงกลุ่มผู้อ่านเฉพาะที่มีข้อกังวลเฉพาะ

ตัวอย่างจุดมองสถาปัตยกรรม มุมมอง และแผนภาพ:

- ขีดความสามารถทางธุรกิจ

- กระบวนการทางธุรกิจระดับสูง

- [สายธารคุณค่า](https://en.wikipedia.org/wiki/Value_stream)

- ฟังก์ชันซอฟต์แวร์ที่จับคู่กับคอมโพเนนต์ของแอปพลิเคชัน

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) แผนภาพบริบท (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) แผนภาพคอนเทนเนอร์ (TO-BE / AS-IS)

- [แผนภาพเอนทิตี-ความสัมพันธ์](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) เพื่อจับคู่เอนทิตีข้อมูลกับคอมโพเนนต์ของแอปพลิเคชัน

- [แผนภาพลำดับ](https://en.wikipedia.org/wiki/Sequence_diagram) เพื่ออธิบายโฟลว์เชิงฟังก์ชันภายในระบบและสำหรับการเชื่อมต่อ

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) แผนภาพเพื่ออธิบายการไหลของข้อมูลข้ามคอมโพเนนต์ของแอปพลิเคชัน

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) แผนภาพเพื่ออธิบายกระบวนการทางธุรกิจ / สถานการณ์ของผู้ใช้

- [การจัดการตัวตนและการเข้าถึง](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) แผนภาพ

- [การควบคุมการเข้าถึงตามบทบาท](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) แผนภาพที่มีบทบาทต่อคอมโพเนนต์ของแอปพลิเคชัน

- [การควบคุมการเข้าถึงตามแอตทริบิวต์](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) แผนภาพที่มีแอตทริบิวต์ต่อคอมโพเนนต์ของแอปพลิเคชัน

- แผนภาพความเป็นส่วนตัว

แผนภาพที่เกี่ยวข้อง:

- แผนภาพยูสเคสแสดงยูสเคสแก่ฝ่ายบริหาร/ลูกค้า ซึ่งมาก่อนข้อกำหนด และข้อกำหนดมาก่อนสถาปัตยกรรมซอฟต์แวร์

- แผนภาพการปรับใช้แสดงฮาร์ดแวร์/คอมพิวเตอร์จริงที่คอมโพเนนต์ซอฟต์แวร์ถูกปรับใช้
- แผนภาพการไหลของข้อมูลแสดงว่าข้อมูลเคลื่อนที่ผ่านระบบและถูกแปลงอย่างไร
- แผนภาพลำดับใช้แสดงว่าโปรโตคอลอย่าง HTTP ทำงานบนแกนเวลาอย่างไร

- แผนภาพกิจกรรมแสดงเวิร์กโฟลว์ของกิจกรรมที่ระบบซอฟต์แวร์ทำ เช่น AI ของ NPC

## ฟังก์ชันความเหมาะสมสำหรับการตัดสินใจในรูปแบบโค้ด

ฟังก์ชันความเหมาะสม (fitness function) คือการตรวจสอบที่เป็นวัตถุวิสัยและอัตโนมัติ เขียนเป็นโค้ดโปรแกรม เพื่อยืนยันว่ามีการปฏิบัติตามการตัดสินใจ

- ฟังก์ชันความเหมาะสมทำให้การตัดสินใจทดสอบได้และรับรองได้

- ฟังก์ชันความเหมาะสมสำหรับการตัดสินใจสามารถช่วยการประกันคุณภาพ กระบวนการกำกับดูแล และเป้าหมายด้านธรรมาภิบาลได้อย่างมาก

### ฟังก์ชันความเหมาะสมและการตัดสินใจเกี่ยวข้องกันอย่างไร

บันทึกการตัดสินใจบันทึกการตัดสินใจ ส่วนฟังก์ชันความเหมาะสมบังคับใช้การตัดสินใจนั้น

- ตัวอย่างการตัดสินใจ: ใช้ event sourcing สำหรับข้อกำหนดด้านการตรวจสอบ

- ตัวอย่างฟังก์ชันความเหมาะสม: ใช้เซิร์ฟเวอร์การรวมระบบอย่างต่อเนื่องเพื่อทดสอบว่าทุกการเปลี่ยนแปลงสถานะต้องสร้างเหตุการณ์

### ทำไมฟังก์ชันความเหมาะสมจึงช่วยการตัดสินใจ

การวัดที่เป็นวัตถุวิสัย: ฟังก์ชันความเหมาะสมผ่านหรือไม่ผ่าน ดังนั้นงานจึงมองเห็นได้และชัดเจน

การใช้งานต่อเนื่อง: ฟังก์ชันความเหมาะสมเป็นกฎที่มีชีวิตและทำงานทุก commit และทุกการสร้าง

ความมั่นใจในการปรับโครงสร้างโค้ด: ฟังก์ชันความเหมาะสมจับข้อผิดพลาดที่ขัดกับกฎการตัดสินใจโดยอัตโนมัติ

การกำกับดูแลที่ปรับขนาดได้: ฟังก์ชันความเหมาะสมบังคับใช้มาตรฐานโดยไม่สร้างคอขวด

### ฟังก์ชันความเหมาะสมใช้ AI ได้หรือไม่

ฟังก์ชันความเหมาะสมสามารถใช้ LLM ของ AI สำหรับการตัดสินใจ โดยถามคำถาม
เกี่ยวกับงานของเรา เช่น แผน โค้ด สคีมา API และอื่น ๆ:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### การทดสอบหน่วยด้านสถาปัตยกรรม

[ArchUnit](https://www.archunit.org/): ตรวจสอบกฎสถาปัตยกรรมของโค้ด Java ด้วยเฟรมเวิร์กการทดสอบหน่วยของ Java ทั่วไป

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): ตรวจสอบกฎสถาปัตยกรรมของโค้ด TypeScript และโค้ด JavaScript ด้วย Jest, Vitest, Jasmine และอื่น ๆ

## ราวกั้นการตัดสินใจสำหรับ pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
นำบันทึกการตัดสินใจที่ถูกต้องขึ้นมาแสดงโดยอัตโนมัติในเวลาที่เหมาะสม คือเมื่อ
นักพัฒนากำลังแก้ไขโค้ดที่การตัดสินใจเหล่านั้นครอบคลุม แทนที่จะหวังว่านักพัฒนา
จะอ่านโฟลเดอร์เอกสารก่อนผสาน บริบทที่เกี่ยวข้องจะปรากฏโดยตรงบน pull request

วิธีนี้ใช้ได้กับบันทึกการตัดสินใจทุกประเภท: การตัดสินใจด้านสถาปัตยกรรม ข้อมูล การปฏิบัติตามข้อกำหนด ทางคลินิกและการแพทย์ ความปลอดภัย และอื่น ๆ

ใช้งานได้กับระบบ CI ใดก็ได้ (GitLab, Jenkins, CircleCI) และเป็น pre-commit hook
โอเพนซอร์ส ไลเซนส์ MIT

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) คือ GitHub
Action ที่ทำให้ pull request ล้มเหลวเมื่อเส้นทางโค้ดที่เฝ้าดูมีการเปลี่ยนแปลงโดยไม่มีบันทึกการตัดสินใจด้านสถาปัตยกรรมถูกเพิ่มหรืออัปเดต การยกเว้นต้องระบุชัดเจน: บรรทัด
`ADR-Exempt:` พร้อมเหตุผลจะผ่านด่านและถูกเขียนลงในสรุปงาน ไม่ผูกกับแม่แบบ ไม่มีการพึ่งพา โอเพนซอร์ส ไลเซนส์ MIT

## ข้อมูลเพิ่มเติม

บทนำ:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

แม่แบบ:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

เจาะลึก:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - บทเรียนสถาปัตยกรรมซอฟต์แวร์รายเดือนฟรี

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

เครื่องมือ:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

แนวทางเฉพาะบริษัท:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

ตัวอย่าง:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

วิดีโอ:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

พอดแคสต์:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

หนังสือ:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

ดูเพิ่มเติม:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - รูปแบบ YAML/JSON ที่เป็นกลางต่อผู้ขายและเครื่องอ่านได้ สำหรับแสดงการตัดสินใจพร้อมเหตุผลที่ชัดเจน สมมติฐาน สภาวะทางปัญญา และการแลกเปลี่ยน ช่วยเสริม ADR โดยเพิ่มเหตุผลที่เป็นโครงสร้างและตรวจสอบได้ลงในเอกสารการตัดสินใจ
