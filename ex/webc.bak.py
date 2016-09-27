
def HEAD():
   h  = """\
     <html> <head> Loading...
     <link rel="stylesheet" type="text/css" href="css/main.css" />
     <!--For versions below Internet Explorer 7-->
     <!--[if lt IE 7]>
     <link rel="stylesheet" href="css/unreal.css" type="text/css">
     <![endif]-->
     <style>.standard_label_style { color: yellow; }</style> </head>
     <body background="img/greent.png">
     <div id="content-wrapper"><div id="content"> <br><br>"""
   return h     

def MAIN():
  h = """\
    <div id="content-wrapper"><div id="content"> 
       <br><br><label><b>
       <label>  Welcome to Things and Stuff</b><pre><br>
       <div>           <img src="img/bwg.png"> </div>
       <div><i> Where Stuff really happens </label></i></div><br>
    </div></div> """
  return h

def FOOT():
  h = """ \
     <div id="footer-wrapper"><div id="footer"><u>
         <a href="buy">buy </a>
         <a href="sell">sell </a>
         <a href="news">news </a>
         <a href="info">info </a>
         <a href="signup">signup </a>
         <a href="login">login </a></u>
     </div></div></body> </html> """
  return h

def TAIL( msg ):
  msg = str( msg )
  h = ''' \
     <div id="header-wrapper"><div id="header">
      <b>''' + msg + '''</b></div></div>
     <div id="footer-wrapper"><div id="footer"><br>\n''' + str( FOOT() )
  return h

def mainpage():
  H = str( HEAD())
  M = str( MAIN() )
  T = str( TAIL('THINGS-N-STUFF') )
  HTML = str( H + '\n' + M + '\n' + T )
  return HTML

def signup():
  def JOIN():
     h  = """\
       <div id="content-wrapper">       <div id="content">
          <br><br><label><b>
          <form action="/confirm" method="post"><pre>
          <div>        First Name:    <input type="text" name="fname" style="width: 200px; height: 25px;">
           <br>         Last Name:    <input type="text" name="lname" style="width: 200px; height: 25px;">
           <br>          Username:    <input type="text" name="user" style="width: 200px; height: 25px;">
           <br>             Email:    <input type="text" name="email" style="width: 200px; height: 25px;">
           <br>          Password:    <input type="password" name="passwda" style="width: 200px; height: 25px;">
           <br>           Confirm:    <input type="password" name="passwdb" style="width: 200px; height: 25px;">
           <br>   Secret Question:    <input type="text" name="squestion" style="width: 200px; height: 25px;">
           <br>     Secret Answer:    <input type="password" name="sanswer" style="width: 200px; height: 25px;">
          <br><input type="checkbox" name="social_x" id="social_x" value="first_checkbox"> Public Contact Info </label>/<b>
         <br><input type="checkbox" id="news_x" name="news_x" value="second_checkbox"><label for="cbox2"> Recieve News Emails </label>
         <br><input type="submit" value="Submit"> <input type="checkbox" id="news_x" name="news_x" value="second_checkbox"> <a href="/tos"> agree to TOS</a><div></div> </div><br></form></pre>
       </div></div> """
     return h
  H = str( HEAD() )
  J = str( JOIN() )
  T = str( TAIL('THINGS-N-STUFF') )
  HTML = str( H + '\n' + J + '\n' + T )
  return HTML

def confirm( cnf ):
  H = str( HEAD() )
  cnf = str( cnf )
  T = str( TAIL('We Accept You, One of Us') )
  HTML = str( H + '\n' + cnf + '\n' + T )
  return HTML

def terms( proc ):
  proc = str( proc )
  def TOS():
     M = """\
       <div id="content-wrapper"><div id="content">
          <br><br><label><b>
          <form action="/" method="post"><pre>
          <label>  All Your Hot Dogs Belong to Us</b></label><br>
          <img src="img/touch.png">
          <br>                    <input type="Back" value="Submit"></form>
       </div></div> """
     H = str( HEAD() )
     T = str( TAIL('THINGS-N-STUFF') )
     HTML = str( H + '\n' + M + '\n' + T )
     return HTML
  t = eval( proc )
  return t()

def portal( proc ):
  proc = str( proc )
  def LOGIN():
     M = """ \
       <div id="content-wrapper"><div id="content">
          <br><br><b><label>What Badges?
                  <pre><label><div>                <img src="img/second.png"><form action="/my-home" method="post"></div>
                  <div>Username:     <input type="text" name="user" style="width: 200px; height: 25px;"></div>
                  <div>Password:     <input type="password" name="passwd" style="width: 200px; height: 25px;"></div>
                  <div>                <input type="submit" value="Submit"></form></div></label></pre>
       </div></div> """
     H = str( HEAD() )
     T = str( TAIL('You dont look framilier...') )
     HTML = str( H + '\n' + M + '\n' + T )
     return HTML
  t = eval( proc )
  return t()

def infro( proc ):
  proc = str( proc )
  def INFO():
     h = """ \
       <div id="content-wrapper"><div id="content"><br><br><b>
          <div>  <label>You made it<pre><label><br>
          <div>                <img src="img/fairy.png"></pre>
       </div></div> """
     return h
  H = str( HEAD() )
  I = str( eval( proc ) )
  T = str( TAIL('THINGS-N-STUFF') )
  HTML = str( H + '\n' + I + '\n' + T )
  return HTML

def myhome( User, proc ):
  User = str( User )
  proc = str( proc )
  def landing():
     L  = """ \
     <div id="content-wrapper"><div id="content"><br><br><b>
       <div><b>  <label>welcome back """ + User + """ </b></label></div>
       <h1><div class="box b"><tr>
            <td style="background-color: green;   padding: 55px;"><input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 55px;"><input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 55px;"><input type="submit" value="test"></td>
          </tr></h1><table cellpadding="0" cellspacing="0">
          <tr>
            <td style="background-color: purple;   padding: 20px;"><p>
            <div><input type="submit" value="test"></div><br>
            <div><input type="submit" value="test"></div><br>
            <div><input type="submit" value="test"></div><br>
            <div><input type="submit" value="test"></div><br>
                       </p></td>
            <td><p>column two </p></td>
            <td><p>

            <div style="width:350px;height:150px;line-height:3em;overflow:scroll;padding:5px;background-color:black;color:orange">
            This 'div' element uses 'overflow:scroll' to create scrollbars whenever the contents of the 'div' become too large.
            <br>frogsix<br><br><br>dsafsa<br><br><br>sdafdsaf<br><br><br>sadfdsafdsa<br><br><br><br><br>asdfsaf<br><br><br>asdfsda 
            </div></p></td></tr><tr>

            <h1><td style="background-color: green;   padding: 25px;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="submit" value="test"> </td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td></h1>
            </tr></table></div></div></div></div>"""
     return L
  H = str( HEAD() )
  M = eval( proc )
  M = str( M() )
  T = str( TAIL('THING-N-STUFF') )
  HTML = str( H + '\n' + M + '\n' + T )
  return HTML 
