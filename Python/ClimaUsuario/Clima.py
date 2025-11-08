import requests
import json

#Este proyecto fue realizado con apoyo de la IA de Gemini de Google.

#API Key de OpenWeather (debes reemplazarla con tu propia clave si es necesario)
OPENWEATHER_API_KEY = "e81ab9acb4f6e640de2ae97ba88dad62" 

def get_weather_from_coords(lat, lon, location_name):
    print(f"\nObteniendo clima para {location_name}...")
    
    url_clima = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    
    try:
        #Esto hace la petición a la API
        response_clima = requests.get(url_clima)
        response_clima.raise_for_status()
        #Esto obtiene los datos en formato JSON
        datos = response_clima.json()
        
        #Extraemos los datos principales
        temp = datos['main']['temp']
        sensacion = datos['main']['feels_like']
        desc = datos['weather'][0]['description']
        humedad = datos['main']['humidity']
        viento_vel = datos['wind']['speed']
        nubosidad = datos['clouds']['all']
        temp_min = datos['main']['temp_min']
        temp_max = datos['main']['temp_max']
        
        #Imprimimos los datos obtenidos
        print(f"\n--- 🌦️ Reporte del Clima: {location_name} ---")
        print(f"Condición: {desc.capitalize()}")
        print(f"🌡️ Temperatura: {temp}°C (Sensación: {sensacion}°C)")
        print(f"📉 Mínima: {temp_min}°C  |  📈 Máxima: {temp_max}°C")
        print(f"💧 Humedad: {humedad}%")
        print(f"💨 Viento: {viento_vel} m/s")
        print(f"☁️ Nubosidad: {nubosidad}%")

    except requests.exceptions.HTTPError as err:
        if "401" in str(err):
            print("\nError FATAL: API Key inválida o no activa.")
        else:
            print(f"Error de HTTP: {err}")
    except Exception as err:
        print(f"Error inesperado: {err}")

def get_location_by_city_name():
    ciudad = input("\nIngresa el nombre de la ciudad/estado (ej. 'Ciudad/Estado, Pais'): ")
    if not ciudad:
        print("No ingresaste un nombre.")
        return

    url_geocoding = f"http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=1&appid={OPENWEATHER_API_KEY}"
    
    try:
        response_geo = requests.get(url_geocoding)
        response_geo.raise_for_status()
        datos_ciudad = response_geo.json()
        
        if not datos_ciudad:
            print(f"Error: No se pudo encontrar la ciudad/estado '{ciudad}'. Intenta ser más específico (ej. 'Quito, EC').")
            return

        lat = datos_ciudad[0]['lat']
        lon = datos_ciudad[0]['lon']
        nombre_encontrado = f"{datos_ciudad[0]['name']}, {datos_ciudad[0]['country']}"
        
        get_weather_from_coords(lat, lon, nombre_encontrado)

    except requests.exceptions.HTTPError as err:
        print(f"Error de HTTP al buscar la ciudad/estado: {err}")
    except Exception as err:
        print(f"Ocurrió un error al buscar la ciudad/estado: {err}")

def get_location_by_ip():
    print("Obteniendo tu ubicación actual (estimada por IP)...")
    
    try:
        response_ip = requests.get("http://ip-api.com/json/")
        response_ip.raise_for_status()
        datos_ip = response_ip.json()
        
        if datos_ip['status'] == 'fail':
            print("Error: El servicio de geolocalización por IP falló.")
            return

        lat = datos_ip['lat']
        lon = datos_ip['lon']
        nombre_encontrado = f"{datos_ip['city']}, {datos_ip['countryCode']}"
        
        get_weather_from_coords(lat, lon, nombre_encontrado)

    except requests.exceptions.HTTPError as err:
        print(f"Error de HTTP al obtener la ubicación IP: {err}")
    except Exception as err:
        print(f"Ocurrió un error al obtener la ubicación IP: {err}")

def main():
    print("--- Servicio de Clima - OpenWeather API ---\n")
    print("¿Cómo quieres obtener el clima?")
    print("  [1] Ingresar el nombre de una ciudad")
    print("  [2] Usar mi ubicación actual (automática por IP)\n")
    while True:
        choice = input("Selecciona una opción (1 o 2): ")
        if choice == '1':
            get_location_by_city_name()
            break
        elif choice == '2':
            get_location_by_ip()
            break
        else:
            print("Opción no válida. Debes escribir '1' o '2'.")

if __name__ == "__main__":
    main()

input("\nPresiona Enter para salir...")