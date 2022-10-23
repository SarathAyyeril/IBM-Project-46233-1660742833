<!DOCTYPE html>
<html>
    <head>
        <title>
            Application Form
        </title>
        <meta name="Aswin" content="application form"></meta>
    </head>
    <body>
        <center>APPLICATION FORM</center>
        <form action="http://localhost:5000/appForm" method="GET">
            <table>
                <tr>
                    <td>
                        <label for="name">NAME :</label>
                    </td>
                    <td>
                        <input id="name" type="text" name="name" placeholder="Enter your name" required/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="email">EMAIL :</label>
                    </td>
                    <td>
                        <input id="email" type="email" name="email" placeholder="Enter your Email" required/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="password">PASSWORD :</label>
                    </td>
                    <td>
                        <input id="password" name="password" type="password" placeholder="Enter Password" required/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="address">ADDRESS :</label>
                    </td>
                    <td>
                        <textarea id="address" name="address" type="address" rows="5" cols="50" placeholder="Enter Adress" required></textarea>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label >GENDER :</label>
                    </td>
                    <td>
                        <input name="gender" type="radio" value="male">Male
                        <input name="gender" type="radio" value="female">Female
                        <input name="gender" type="radio" value="others">Others
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="country">COUNTRY :</label>
                    </td>
                    <td>
                        <select name="country" id="country">
                            <option value="india">Indian</option>
                            <option value="non-indian">non-Indian</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>
                    <input id="submit" type="submit" name="submit"/>
                    </td>
                </tr>
            </table>
        </form>
    </body>
</html
