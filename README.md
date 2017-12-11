# Autogger Project

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
5. Create `local_settings.py` file in `$SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/autogger/autogger` folder. Sample `local_settings.py` file can be found here: `$SYSTEM_ROOT_GIT_REPO_FOLDER/autogger/autogger/autogger/not_local_settings_file.py`.
6. Run `al_psql_reset` from command line.
8. Run `al_init_data_load` from command line.
7. Run `al_bcr develop` from command line.

You're now all set.
