
<head>

<title>Login Page</title>
 
</head>
 
<body bgcolor = "powderblue">
    <form action = login.html method="post">
    <table border="2" align="center" bgcolor="skyblue">
    <tr>
    <td colspan="2" align="center">Login Form</td>
    </tr>

    <tr>
    <td>Username:</td>
    <td><input type ="text" name="user"></td>
    </tr>    

    <tr>
    <td>Password:</td>
    <td><input type ="text" name="pass"></td>
    </tr>        

        <tr>
        <td colspan="2" align="center"><input type="submit" name="submit" value="submit"></td>
        </tr>
    </table>
    </form>
</body>
</html>
<?php
mysql_connect("localhost","root","");
mysql_select_db("login");

if(isset()$_POST['submit'])
    {
        $username = $_POST['user'];
        $password = $_POST['pass'];

        $query = "insert into login (Username, Password) values ('$username', '$password");
        if(mysql_query($query))
        {
            echo "You have successfully logged in";
        }
    }
    
?>