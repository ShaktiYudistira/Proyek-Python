import http.client
import json

# Dictionary for translating weather descriptions from English to Indonesian
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds': 'berawan',
    'overcast clouds': 'mendung',
    'moderate rain': 'hujan sedang',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',
    'rain': 'hujan',
    'thunderstorm': 'badai petir',
    'snow': 'salju',
    'mist': 'kabut'
}

def ambil_data_cuaca(kota, api_key):
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    url = f"/data/2.5/forecast?q={kota}&appid={api_key}&units=metric"
    
    conn.request("GET", url)
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        return json.loads(data)
    else:
        print(f'Error {response.status}: {response.reason}')
        return None

def analisis_cuaca(data):
    if data is None:
        return None
    
    forecast_list = data.get('list', [])
    hasil = {}

    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]
        temp = item['main']['temp']
        humidity = item['main']['humidity']
        desc = item['weather'][0]['description']
        desc_id = deskripsi_cuaca_id.get(desc, desc)

        if date not in hasil:
            hasil[date] = {
                'Temperatur (°C)': [],
                'Kelembapan (%)': [],
                'Deskripsi Cuaca': []
            }
        
        hasil[date]['Temperatur (°C)'].append(temp)
        hasil[date]['Kelembapan (%)'].append(humidity)
        hasil[date]['Deskripsi Cuaca'].append(desc_id)

    # Calculate daily averages
    for date in hasil:
        hasil[date]['Temperatur (°C)'] = sum(hasil[date]['Temperatur (°C)']) / len(hasil[date]['Temperatur (°C)'])
        hasil[date]['Kelembapan (%)'] = sum(hasil[date]['Kelembapan (%)']) / len(hasil[date]['Kelembapan (%)'])
        hasil[date]['Deskripsi Cuaca'] = max(set(hasil[date]['Deskripsi Cuaca']), key=hasil[date]['Deskripsi Cuaca'].count)

    return hasil

def main():                                          
    
    kota = input('Masukkan nama kota: ')
    api_key = '41d6c3c08f6771bff1fc7ccbe33c53bf'  # Replace with your API key

    data = ambil_data_cuaca(kota, api_key)
    hasil = analisis_cuaca(data)

    if hasil is not None:
        print("Hasil Analisis Cuaca:")
        for date, details in hasil.items():
            print(f"{date}: Temperatur (°C) = {details['Temperatur (°C)']:.2f}, "
                  f"Kelembapan (%) = {details['Kelembapan (%)']:.2f}, "
                  f"Deskripsi Cuaca = {details['Deskripsi Cuaca']}")

if __name__ == '__main__':
    main()