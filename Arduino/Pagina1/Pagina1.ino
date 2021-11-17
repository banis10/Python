#include <ESP8266WiFi.h>

int out1 = 2; 
int out2 = 0;
int out3 = 4;
int out4 = 5;

String ssid     = "TooL";
String password = "Lateralus_AEnima_10000Days";
WiFiServer server(80); //objeto de la clase WiFiServer
int estado1 = 0;
int estado2 = 0;
int estado3 = 0;
int estado4 = 0;

void setup() {
  // Inicia Serial
  Serial.begin(115200);
  Serial.println("\n");

  pinMode(out1,OUTPUT);
  pinMode(out2,OUTPUT);
  pinMode(out3,OUTPUT);
  pinMode(out4,OUTPUT);

  // Conexión WIFI
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED ) { 
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("********************************************");
  Serial.print("Conectado a la red WiFi: ");
  Serial.println(WiFi.SSID());
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("macAdress: ");
  Serial.println(WiFi.macAddress());
  Serial.println("*********************************************");
  
  server.begin(); //begin() levantamos el servidor 
  digitalWrite(out1, 0);
  digitalWrite(out2, 0);
  digitalWrite(out3, 0);
  digitalWrite(out3, 0);
  
}

void loop() {
  
  WiFiClient client = server.available(); //objeto de la clase WiFiClient
  // avalaible() detecta un cliente nuevo del objeto de la clase WifiServer
  if(!client){
    return;
  }
  
  Serial.println("Nuevo cliente...");
  while(!client.available()){ //espera a un cliente diponible
    delay(1);
  }

  String peticion = client.readStringUntil('\r'); //lee la peticion del cliente
  Serial.println(peticion);
  client.flush(); //limpia la peticion del cliente

  if(peticion.indexOf("tv1=ON") != -1)
  {
    estado1=1;
  }
  if(peticion.indexOf("tv1=OFF") != -1)
  {
    estado1=0;
  }
  digitalWrite(out1, estado1);

  if(peticion.indexOf("tv2=ON") != -1)
  {
    estado2=1;
  }
  if(peticion.indexOf("tv2=OFF") != -1)
  {
    estado2=0;
  }
  digitalWrite(out2, estado2);

  if(peticion.indexOf("tv3=ON") != -1)
  {
    estado3=1;
  }
  if(peticion.indexOf("tv3=OFF") != -1)
  {
    estado3=0;
  }
  digitalWrite(out3, estado3);

  if(peticion.indexOf("tv4=ON") != -1)
  {
    estado4=1;
  }
  if(peticion.indexOf("tv4=OFF") != -1)
  {
    estado4=0;
  }
  digitalWrite(out4, estado4);



  client.println("HTTP/1.1 200 OK");
  client.println("");
  client.println("");
  client.println("");
  client.println(""); 

    //INICIA LA PAGINA

client.println("<!DOCTYPE html>");
client.println("<html lang='en'>");
client.println("<head>");
    client.println("<meta charset='UTF-8'>");
    client.println("<meta name='viewport' content='width=device-width, initial-scale=1.0'>");
    client.println("<title>Control splitter</title>");
    client.println(" <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We' crossorigin='anonymous'>");


client.println("</head>");
client.println("<center>");
   client.println("<h1>Control de Pantallas</h1>");

client.println("</center>");

client.println("<body style='font-family: Century gothic; width: 800;'>");
    client.println("<center>");
    client.println("<div style='box-shadow: 0px 0px 20px 8px rgba(0,0,0,0.22); padding: 20px; width: 300px; display: inline-block; margin: 30px;'> ");
        client.println("<h1>Sala 1</h1>");

  if(estado1 == 1)
  {
       client.println(" <h2 style='color:MediumSeaGreen;'>Encendida</h2>");
  }
  if(estado1 == 0)
  {
       client.println(" <h2 style='color:Tomato;'>Apagada</h2>");
  }

  
       client.println("<button type='button' onClick=location.href='/tv1=ON' class='btn btn-outline-success'>Encender</button>");
       client.println("<button type='button' onClick=location.href='/tv1=OFF' class='btn btn-outline-danger'>Apagar </button> ");

       
  client.println("  </div>");

  client.println("  <div style='box-shadow: 0px 0px 20px 8px rgba(0,0,0,0.22); padding: 20px; width: 300px; display: inline-block; margin: 30px;'> ");
   client.println("     <h1>Sala 2</h1>");
  if(estado2 == 1)
  {
       client.println(" <h2 style='color:MediumSeaGreen;'>Encendida</h2>");
  }
  if(estado2 == 0)
  {
       client.println(" <h2 style='color:Tomato;'>Apagada</h2>");
  }

   
       client.println("<button type='button' onClick=location.href='/tv2=ON' class='btn btn-outline-success'>Encender</button>");
       client.println("<button type='button' onClick=location.href='/tv2=OFF' class='btn btn-outline-danger'>Apagar </button> ");

 client.println("   </div>");
client.println("    </center>");
client.println("</body>");

client.println("<body style='font-family: Century gothic; width: 800;'>");
    client.println("<center>");
    client.println("<div style='box-shadow: 0px 0px 20px 8px rgba(0,0,0,0.22); padding: 20px; width: 300px; display: inline-block; margin: 30px;'> ");
        client.println("<h1>Sala 3</h1>");
  if(estado3 == 1)
  {
       client.println(" <h2 style='color:MediumSeaGreen;'>Encendida</h2>");
  }
  if(estado3 == 0)
  {
       client.println(" <h2 style='color:Tomato;'>Apagada</h2>");
  }

       
       client.println("<button type='button' onClick=location.href='/tv3=ON' class='btn btn-outline-success'>Encender</button>");
       client.println("<button type='button' onClick=location.href='/tv3=OFF' class='btn btn-outline-danger'>Apagar </button> ");


       
  client.println("  </div>");

  client.println("  <div style='box-shadow: 0px 0px 20px 8px rgba(0,0,0,0.22); padding: 20px; width: 300px; display: inline-block; margin: 30px;'> ");
   client.println("     <h1>Sala 4</h1>");
  if(estado4 == 1)
  {
       client.println(" <h2 style='color:MediumSeaGreen;'>Encendida</h2>");
  }
  if(estado4 == 0)
  {
       client.println(" <h2 style='color:Tomato;'>Apagada</h2>");
  }
       client.println("<button type='button' onClick=location.href='/tv4=ON' class='btn btn-outline-success'>Encender</button>");
       client.println("<button type='button' onClick=location.href='/tv4=OFF' class='btn btn-outline-danger'>Apagar </button> ");


  
 client.println("   </div>");
client.println("    </center>");
client.println("</body>");


         
    //FIN DE LA PAGINA

  delay(5);
  Serial.println("Peticion finalizada");
  Serial.println("");  
}
