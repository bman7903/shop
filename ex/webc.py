from re import sub

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

def preadd( ustr, stuff ):
  ustr  = str( ustr )
  item  = str( stuff[0] )
  gory  = str( stuff[1] )
  subc  = str( stuff[2] )
  desc  = str( stuff[3] )
  price = str( stuff[4] )
  ship  = str( stuff[5] ) 
  img1  = str( stuff[6] )
  img2  = str( stuff[7] )
  img3  = str( stuff[8] )
  pcs   = str( stuff[9] )
  lts   = str( stuff[10] )
  info  = str( stuff[11] ) 

  def mid():
     h = ''' \
       <div id="content-wrapper"><div id="content"><br><br><b>
          <div><label><b>''' + item + '''</b><pre>
          <div><u><b>Description</u>:</b> ''' + desc + '''</div></pre>
          <div><center>  <a href="''' + img1 + '''" ><img src="''' + img1 + '''" width="128" height="128"></a>&nbsp&nbsp&nbsp&nbsp
           <a href="''' + img2 + '''"><img src="''' + img2 + '''" width="128" height="128"></a>&nbsp&nbsp&nbsp&nbsp
           <a href="''' + img3 + '''"><img src="''' + img3 + '''" width="128" height="128"></a></center></div>
          <div><u><b>Category</u>:</b> <i>''' + gory + '''</i>  <b><u>sub-Category</u>:</b> <i>''' + subc + '''</i></div> 
          <div><u><b>Price</u> <u>USD</u>:</b> $''' + price + '''  <b><u>Shipping</u>:</b> $''' + ship + '''</div>
          <div><u><b>Pieces Per</u>:</b> ''' + pcs + ''' <b><u>Total Pieces</u>:</b> ''' + lts + '''</div>   
          <div><u><b>Info</u>:</b> <i>''' + info + '''<i></div></label><br>

          <pre><div> If this looks right please <form action="/my-home" method="post"><input type="hidden" name="uzer" value="''' + ustr + '''"><input type="submit" value="Continue"> or <form action="/my-add" method="post"><input type="hidden" name="uzer" value="''' + ustr + '''"><input type="submit" value="Edit"> or <form action="/my-del" method="post"><input type="hidden" name="uzer" value="''' + ustr + '''"><input type="submit" value="Delete"></form></form></form></div></pre>
       </div></div> '''
     return h

  H = str( HEAD() )
  I = str( mid() )
  T = str( TAIL('THINGS-N-STUFF') )
  HTML = str( H + '\n' + I + '\n' + T )
  return HTML

def preerr( ers ):
  ers = str( ers )
  def mid():
     h = ''' \
       <div id="content-wrapper"><div id="content"><br><br><b>
          <div>  <label>You made it<pre><label><br>
          <div>                <img src="img/fairy.png"></pre><br>
          <div>  You selected ''' + ers + ''' </div>
       </div></div> '''
     return h

  H = str( HEAD() )
  I = str( mid() )
  T = str( TAIL('THINGS-N-STUFF') )
  HTML = str( H + '\n' + I + '\n' + T )
  return HTML

def myhome( User, ustr, lots, proc ):
  User = str( User )
  ustr = str( ustr )
  proc = str( proc )
#  lots = lots
  def landing():
     t = ''
     for l in lots:
       l = str( l )
       n = str( l.split('$')[0] ).strip()
       l = str('<input type="checkbox" name="modify" value="' + n + '">' + l )
       if '<br>' in t:
          t = str( t + '<br>' + l )
       else:
          t = str( l + '<br>' )
     t = str( sub('<br><br>','<br>',t) )
     L  = ''' \
     <div id="content-wrapper"><div id="content"><br><br><b>
       <div><b>  <label>welcome back ''' + User + ''' </b></label></div>
       <h1><div class="box b"><tr>
            <td style="background-color: green;   padding: 55px;"><form action="home-add" method="post"><input type="submit" value="Add"></td><input type="hidden" name="uzer" value="''' + ustr + '''">
            <td style="background-color: green;   padding: 55px;"><form action="home-del" method="post"><input type="submit" value="Del"></td>
            <td style="background-color: green;   padding: 55px;"><form action="home-add" method="post"><input type="submit" value="Edit"></td>
          </tr></h1><table cellpadding="0" cellspacing="0">
          <tr>
            <td style="background-color: purple;   padding: 20px;"><p>
            <div><input type="submit" value="text"></div><br>
            <div><input type="submit" value="test"></div><br>
            <div><input type="submit" value="test"></div><br>
            <div><input type="submit" value="test"></div><br>
            </p></td><td><p>" "</p></td><td><p>

            <div style="width:450px;height:190px;line-height:3em;overflow:scroll;padding:5px;background-color:black;color:orange">
            ''' + str( t ) + ''' </div></p></td></tr></form></form></form><tr>

            <h1><td style="background-color: green;   padding: 25px;">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="submit" value="test"> </td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td>
            <td style="background-color: green;   padding: 25px;"> <input type="submit" value="test"></td></h1>
            </tr></table></div></div></div></div>'''
     return L

  def add():
     M  = '''\
       <div id="content-wrapper">       <div id="content">
          <br><br><label><b>
          <form action="/pre-add" method="post"><pre>
          <input type="hidden" name="uzer" value="''' + ustr + '''">
          <div>        item:    <input type="text" name="item" style="width: 200px; height: 25px;">
           <br>    category:    <input type="text" name="cat" style="width: 200px; height: 25px;">
           <br>sub-Category:    <input type="text" name="sub-cat" style="width: 200px; height: 25px;"> *
           <br> Description:    <input type="text" name="desc" style="width: 200px; height: 25px;">
           <br>   Price USD:    <input type="text" name="price" style="width: 200px; height: 25px;">
           <br>    Shipping:    <input type="text" name="shipping" style="width: 200px; height: 25px;"> *
           <br> Image 1 URL:    <input type="text" name="image1" style="width: 200px; height: 25px;">
           <br> Image 2 URL:    <input type="text" name="image2" style="width: 200px; height: 25px;"> *
           <br> Image 3 URL:    <input type="text" name="image3" style="width: 200px; height: 25px;"> *
           <br>  Pieces Per:    <input type="text" name="pieces" style="width: 200px; height: 25px;">
           <br>  Total Lots:    <input type="text" name="lots" style="width: 200px; height: 25px;"> *
           <br>        Info:    <input type="text" name="more" style="width: 200px; height: 25px;"></label> *
         <br><input type="submit" value="Submit"></div></form></pre>
       </div></div> '''
 #    lots = str( lots )
 #    if not 'None' in lots:
     M = str( M + ' ' + str( lots ) )
     return M

  def remove():
     html = 'Good Job Remove'
     return html
  def dupe():
     html = 'Good Job Dupe!'
     return html

  H = str( HEAD() )
  M = eval( proc )
  M = str( M() )
  T = str( TAIL('THING-N-STUFF') )
  HTML = str( H + '\n' + M + '\n' + T )
  return HTML
