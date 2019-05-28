Notipy Me
=========

A simple python package to send you and any other receiver an email when a portion of code is done running.

Setup
-----

Just run:

.. code:: bash

   pip install notipy_me

Usage example
-------------
A basic usage example can be the following:

Usage as decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from notipy_me import Notipy

    @Notipy("Long running script", "my_mail@myserver.com", send_start_mail=True)
    def my_long_running_script():
        ...

Usage as context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from notipy_me import Notipy

    with Notipy("Long running script", "my_mail@myserver.com", send_start_mail=True):
        my_long_running_script()

Setting the mail password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script will ask you to insert the email password, and then you'll be set to go:

.. code:: bash

    Please insert your email password:

Some additional settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
All the available settings are the following:

.. code:: python

    Notipy(
        task="task name", # name of the task you are executing.
        email="my_mail@myserver.com", # email from which send the emails.
        recipients=None, # List of recepients.
        port=465, # Server port, default one for using SSL.
        server=None, # SMTP server.
        send_start_mail=False # Whetever to send or not also a mail when the task starts.
    )

Known issues
------------

Gmail
~~~~~
I cannot manage to get gmail to work, but it keeps rising an error
logging in with the credentials, even though they are correct. With the
other mail providers it works fine.