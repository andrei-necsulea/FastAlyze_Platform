import pandas as pd



def read_csv(df):
 
 def verify_integer_list(lista):
     if all( isinstance(item , int) for item in lista) or all( isinstance(item , float) for item in lista) or all( isinstance(item , complex) for item in lista) :
      return True
     else:
      return False
     
 def string_is_number(string_var): 
   
   def is_float():
     try:
        float(string_var)
        return True
     except ValueError:
        return False           

   def is_int():
       try:
           int(string_var)
           return True
       except ValueError:
           return False

   def is_complex():
       try:
           complex(string_var)
           return True
       except ValueError:
           return False 

   if is_float() == True :
       return True
       
   
   if is_int() == True :
       return True
       
    
   if is_complex() == True :
       return True
      
   
   if is_float() == False and is_int() == False and is_complex() == False :
       return False
          
     

 data_frame_list = []
 for i in list(df):
    data_frame_list.append(df[i].tolist())


 for i in range(0,len(data_frame_list),1):
        if verify_integer_list(data_frame_list[i]) == False :
                          for j in range(0,len(data_frame_list[i])-1,1):
                               aux = data_frame_list[i][j]
                               if string_is_number(aux) == False :
                                    data_frame_list[i].remove(aux)    
             
        
         
        
 return data_frame_list

     