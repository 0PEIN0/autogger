cd autogger
#find . -name '*.pyc' -delete
if [ -d "uploads" ]; then
  echo "Upload directory exists!"
else
  mkdir uploads
fi;
python manage.py heroku_deploy
#./manage.py shell < scripts/init_data_loader.py
gunicorn autogger.wsgi --timeout 300 --limit-request-line 8190 --limit-request-fields 200 --limit-request-field_size 8190 --keep-alive 5 --log-file -
