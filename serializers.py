
class SerializerClass:
    
    def serializer_property(self,query):
      fields = ('id','descripcion','direccion','ciudad','año','precio','estado')

      dict_field = {}
      list_dict_field = []
      for row in query:
          i=0
          for field in fields:
              dict_field[field]=row[i]
              i+=1
          list_dict_field.append(dict_field)
      return list_dict_field


