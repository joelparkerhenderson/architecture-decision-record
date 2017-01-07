# ADR Start

Here's how to start using ADRs for a typical software project.

1. Create a directory for documentation and ADR files.

      mkdir doc/adr

2. For each ADR, create a text file, such as `database.txt`.

      vi database.txt

3. Write anything you want in the ADR. See the templates in this repo for ideas.


## Extra ideas

We prefer to use a file name that has a specific format.

  * The name has the date as YYYYMMDD. This is useful for sorting.

  * The name has a present tense imperative verb phrase. This is useful for reading.

  * The name uses lowercase letters and underscore separators.

  * The extension is markdown.

Examples:

    20170101_choose_a_database.md
    20170102_handle_more_users.md
    20170103_strengthen_security.md
    20170104_improve_energy_efficiency.md
