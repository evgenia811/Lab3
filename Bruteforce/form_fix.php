<?php
if( isset($_POST['Login']) && isset($_POST['username']) && isset($_POST['password']) ) {
	
    $user = $_POST['username'];

    $total_failed_login = 3;  
    $lockout_time       = 5;  
    $account_locked     = false; 

    $data = $db->prepare( 'SELECT id, failed_login, last_login, email, unlock_token FROM users WHERE user = (:user) LIMIT 1;' );  
    $data->bindParam( ':user', $user, PDO::PARAM_STR );  
    $data->execute();  
    $row = $data->fetch();	
 
    if (($data->rowCount() == 1) && ($row['failed_login'] >= $total_failed_login) && ($row['unlock_token'] == NULL)) {  
	
        $last_login = strtotime( $row[ 'last_login' ] );  
        $timeout    = $last_login + ($lockout_time * 60);  
        $timenow    = time();  

        if( $timenow < $timeout ) {  
            $account_locked = true;  
        }  
    }  
	
	$passwd = $_POST['password']
	$black_list_passwd = file('passwords.txt');
	foreach ($black_list_passwd as $line_num => $black_passwd) {
		if ($black_passwd == $passwd)
			$email = $row['email']
			$uniqid_token = uniqid();
			$url = ((!empty($_SERVER['HTTPS'])) ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
			$url = explode('?', $url);
			$url = $url[0];
			$url = $url . '?' . (string)$uniqid_token
			$data = $db->prepare( 'UPDATE users SET unlock_token = '$uniqid_token' WHERE id = '$row['id']'');  
			$message = 'Ваша учётная запись была скомпрометирована, для защиты аккаунта он был заблокирован, перейдите по ссылке {$url} для воостановления доступа'
			mail($email, 'Восстановление доступа', $message);
	}

    $pass = sha256( $passwd, get_salt($user));  

    $data = $db->prepare( 'SELECT * FROM users WHERE user = (:user) AND password = (:password) LIMIT 1;' );  
    $data->bindParam( ':user', $user, PDO::PARAM_STR);  
    $data->bindParam( ':password', $pass, PDO::PARAM_STR );  
    $data->execute();  

    $row = $data->fetch();

    $html = "";

    if( ( $data->rowCount() == 1 ) && ( $account_locked == false ) ) {  
        $avatar = $row[ 'avatar' ];  

        $html .= "<p>Welcome to the password protected area {$user}</p>";  
        $html .= "<img src=\"{$avatar}\" />";  

        $failed_login = $row[ 'failed_login' ];  
        $data = $db->prepare( 'UPDATE users SET failed_login = "0" WHERE user = (:user) LIMIT 1;' );  
        $data->bindParam( ':user', $user, PDO::PARAM_STR );  
        $data->execute();  
    } else {  
        sleep(3);  

        $html .= "<pre>";
        $html .= "Username and/or password incorrect.<br/><br/>";
        $html .= "This account has been blocked for too many login attempts.<br/>";
        $html .= "Please try again in {$lockout_time} minutes<br/>";

        $data = $db->prepare( 'UPDATE users SET failed_login = (failed_login + 1) WHERE user = (:user) LIMIT 1;' );  
        $data->bindParam( ':user', $user, PDO::PARAM_STR );  
        $data->execute();  
    }

    $data = $db->prepare( 'UPDATE users SET last_login = now() WHERE user = (:user) LIMIT 1;' );  
    $data->bindParam( ':user', $user, PDO::PARAM_STR );  
    $data->execute();
}
else {
	$url = $_SERVER['QUERY_STRING'];
	$url = explode('=', $url);
	$unlock_token = $url[1]
	
	$data = $db->prepare( 'SELECT id FROM users WHERE unlock_token = '$unlock_token';' );   
    $data->execute();  
    $row = $data->fetch();
	$data = $db->prepare( 'UPDATE users SET unlock_token = NULL WHERE id = '$row['id']'');  
}
?>