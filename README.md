<h1>Trace feedback bot.(@tracefeedbackbot)</h1>

<h2>Installation.</h2>

<code> git clone https://github.com/tracemoepy/tracefeedback.git</code>

<code> cd tracefeedback/</code>

<h3>Install mongodb.</h3>
<nav>
<li><b><a href='https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/'>Debian.</a></b></li>
<li><b><a href='https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/'>Ubuntu.</a></b></li></br>
</nav>


<code> pip3 install -r requirements.txt</code></br>


<h3>Now you must insert your values into config.ini</h3>


<b>1. bot_token - Your bot token.</b></br>
<b>2. db_url - Use mongodb://localhost:27017 to run the database on the local machine</br>Or use MongoDB URI <a href='https://telegra.ph/How-To-get-Mongodb-URI-06-26'>(I wrote how to get it in this article).</b></a></br>


<code> python3 main.py</code>
