# flask-with-db

While my application seems to run, the landing page loads an error page:

Below is the error I get each time I try to load the page

AttributeError
AttributeError: 'function' object has no attribute 'execute'

Traceback (most recent call last)
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 2548, in __call__
return self.wsgi_app(environ, start_response)
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 2528, in wsgi_app
response = self.handle_exception(e)
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 2525, in wsgi_app
response = self.full_dispatch_request()
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 1822, in full_dispatch_request
rv = self.handle_user_exception(e)
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 1820, in full_dispatch_request
rv = self.dispatch_request()
File "C:\Users\izaak\.pyenv\pyenv-win\versions\3.9.13\lib\site-packages\flask\app.py", line 1796, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
File "C:\Users\izaak\Documents\AHI_PROJECTS\DB_Sqlite\app.py", line 17, in index
patientListSql = conn.execute("SELECT * FROM patient_table").fetchall()
AttributeError: 'function' object has no attribute 'execute'
The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.
To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

dump() shows all variables in the frame
dump(obj) dumps all that's known about the object
