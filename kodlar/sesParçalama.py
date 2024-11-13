from pydub import AudioSegment
import os

input_folder = "C:/Users/fanat/Desktop/yazLab/kuşSesleri/karaŞahin"  # Klasör adını buraya yazın
output_folder = "C:/Users/fanat/Desktop/yazLab/kuşSesleri/karaŞahin(parçalanmış)"
os.makedirs(output_folder, exist_ok=True)

segment_duration = 10 * 1000  # milisaniye cinsinden (10 saniye)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp3"):
        file_path = os.path.join(input_folder, file_name)
        try:
            audio = AudioSegment.from_mp3(file_path)
            audio_length = len(audio)
            for i in range(0, audio_length, segment_duration):
                segment = audio[i:i + segment_duration]
                output_file = os.path.join(output_folder,
                                           f"{os.path.splitext(file_name)[0]}_segment_{i // 1000}-{(i + len(segment)) // 1000}.mp3")
                segment.export(output_file, format="mp3")
                print(f"{output_file} oluşturuldu.")
        except Exception as e:
            print(f"Dosya işlenirken hata oluştu: {file_name}, Hata: {e}")

print("Tüm ses dosyaları başarıyla bölündü.")
