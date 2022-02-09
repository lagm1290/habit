from connection import Connection
from serializers import SerializerClass

class ControllerClass:
    
    def list_property(self,kwargs):
        result_serializer = None
        result_data = None
        query = """
                    SELECT sh.property_id as id , max(p.description) as descripcion,
                    max(p.address) as direccion, max(p.city) as ciudad,max(p.year) as ano,
                    max(p.price) as precio,max(s.name) as estado  
                    FROM status_history sh inner join property p 
                    on sh.property_id = p.id inner join status s 
                    on sh.status_id = s.id 
                    WHERE s.name in ('pre_venta','en_venta','vendido')
                    GROUP BY sh.property_id 
                    
                """
        order = " ORDER BY sh.id DESC;"
        i = 0
        for key , value in kwargs.items():
            if key in ['ciudad','ano','estado']:
                if i == 0:
                    query += "HAVING "
                else:
                    query += " AND "
                
                if key =='ciudad':
                    query += "{}='{}'".format(key, value)
                elif key =='ano':
                    query += "{}={}".format(key, value)
                elif key == "estado":
                    query += "{}='{}'".format(key, value)
            i +=1
        query +=order
        # se manda a ejecutar el método de conexion a la bd y a la vez se ejecuta la consulta
        result_data = Connection.query(self, query)
        # se realiza la serialización del resultado de la consulta
        result_serializer = SerializerClass.serializer_property(self,result_data)
    
        return result_serializer