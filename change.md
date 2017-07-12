Change
-Modify "settings.py", change "DATABASES" , to "'django.db.backends.postgresql_psycopg2'".
-Modify "talks/urls.py", add "url(r'^session-list/', views.session_list_view, name = 'sessions')".
-Modify "talks/views.py", modify/add "session_list_view" .
-Add "session.html" to "podium/templates/talks" 
