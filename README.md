# Autogger Project

#### Project Stacks:
1. Django 2.0
2. Postgres 9.6
3. Angular 5

#### Setup Instructions:

1. Make sure that [bash-helpers](https://github.com/0PEIN0/bash-helpers) repository is cloned on local machine.
2. Add the following lines in the `personal.sh`(reference can be found in `bash-helpers` repository) file. Don't forget to source it after adding the import below. You can source it by running this command: `source ~/.bashrc` in case of bash shell or `source ~/.zshrc` in case of ZSH shell.
```bash
if [ -f $SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/scripts/autogger-project-core.sh ]; then
    . $SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/scripts/autogger-project-core.sh
fi;
```
3. Run `al_ve_init` from command line.
4. Run `al_ve_installs` from command line.
5. Create `local_settings.py` file in `$SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/autogger/autogger` folder. Example `local_settings.py` file can be found here: `$SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/autogger/autogger/not_local_settings_file.py`(don't use this file directly). Change necessary variable values in the `local_settings.py` file like `DJANGO_ADMIN_SUPER_USER_EMAIL` property, postgres username/password etc.
6. Run `al_postgres_user_password_reset` from command line.
7. Run `al_psql_reset` from command line.
8. Run `al_ve` from command line.
9. Run `./manage.py makemigrations` from command line.
10. Run `./manage.py migrate` from command line.
11. Run `al_init_data_load` from command line.
12. Run `al_bcr develop` from command line. This command will start up the project on `8090` port. Visit ***http://localhost:8090/admin/*** to browse django admin.

You're now all set.
