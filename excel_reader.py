import pandas as pd



def read_xlsx(df):
    
    def verify_integer_list(lista):
       if all( isinstance(item , int) for item in lista) or all( isinstance(item , float) for item in lista) or all( isinstance(item , complex) for item in lista) :
         return True
       else:
         return False
       

    data_frame_list = []   
    for i in range(len(list(df[df.columns]))):
        data_frame_list.append(list(df[df.columns[i]]))  


    for i in range(0,len(data_frame_list),1):
        if verify_integer_list(data_frame_list[i]) == False :
                          for j in range(0,len(data_frame_list[i])-1,1):
                               aux = data_frame_list[i][j]
                               if type(aux) == str :
                                    data_frame_list[i].remove(aux)
                      
    return data_frame_list  