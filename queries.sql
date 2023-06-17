call new_client("dale2", "dale2@email.com","password",
"https://images.pexels.com/photos/9091291/pexels-photo-9091291.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", 
"my name is dale1 and this is my bio.");

call w22b.login("dale2", "password", "randomfaketoken1");

call delete_token("randomfaketoken1");

call w22b.get_profile("randomfaketoken1");
