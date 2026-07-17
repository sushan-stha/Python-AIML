# Password Authenticator-->logic buidling
secret_password = "stha.sushan"
attempts = 0
max_attempts = 3
while(attempts < max_attempts):
        user_input = input("Enter your secret password to contiue:")
        if(secret_password == user_input):
            print("Access Granted!!😍")
            break
        else:
            print("Access Denied")
            attempts +=1
        
        if(attempts == max_attempts):
             print("Account Blocked!!🥲")

        
        

        
        
            
            
            
            
        
        

        
