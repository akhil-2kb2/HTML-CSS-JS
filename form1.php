<!DOCTYPE html>
<html>
<head>
    <title>First Form</title>
</head>
<body>

    <table align="center" border="0" cellpadding="10" cellspacing="0">
        <tr>
            <th colspan="2">
                <h2>Form 1: Input Data</h2>
            </th>
        </tr>
        <form action="form2.php" method="POST">
            <tr>
                <td><label for="name">Name:</label></td>
                <td><input type="text" id="name" name="name" required></td>
            </tr>
            <tr>
                <td><label for="email">Email:</label></td>
                <td><input type="email" id="email" name="email" required></td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    <input type="submit" value="Submit">
                </td>
            </tr>
        </form>
    </table>

</body>
</html>
