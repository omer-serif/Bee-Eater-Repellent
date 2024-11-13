from pydub import AudioSegment, effects
import os
import scipy.signal
import noisereduce as nr
import numpy as np
import scipy.fftpack

input_folder = "C:/Users/fanat/Desktop/yazLab/kuşSesleri/arıKuşu(parçalanmış)"
output_folder = "C:/Users/fanat/Desktop/yazLab/kuşSesleri/arıKuşu(tamamlanmış)"
os.makedirs(output_folder, exist_ok=True)

# MFCC Hesaplama Fonksiyonu
def calculate_mfcc(y, sr, n_mfcc=13):
    # STFT hesaplama
    n_fft = 2048
    hop_length = 512
    S = np.abs(scipy.signal.stft(y, sr, nperseg=n_fft, noverlap=hop_length)[2]) ** 2

    # Mel filtrebank hesaplama
    mel_bins = 128
    fmin, fmax = 0, sr // 2
    mel_basis = np.zeros((mel_bins, S.shape[0]))

    # Mel filterbank oluşturma
    for i in range(mel_bins):
        freq = fmin + (fmax - fmin) * (i / (mel_bins - 1))
        mel_basis[i, :] = np.sin((np.pi / 2) * (freq / (sr / 2)))

    mel_S = np.dot(mel_basis, S)

    # Logaritmik ölçekte mel spektrum
    log_mel_S = np.log(mel_S + 1e-9)

    # MFCC hesaplama
    mfcc = scipy.fftpack.dct(log_mel_S, axis=0, norm='ortho')[:n_mfcc]
    return mfcc

# Tüm mp3 dosyalarını dolaş
for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp3"):
        file_path = os.path.join(input_folder, file_name)

        # Ses dosyasını yükle
        audio = AudioSegment.from_mp3(file_path)

        # Gürültü Temizleme
        y = np.array(audio.get_array_of_samples())
        sr = audio.frame_rate
        reduced_noise = nr.reduce_noise(y=y, sr=sr)

        # Ses Normalizasyonu
        normalized_audio = effects.normalize(AudioSegment(
            reduced_noise.tobytes(),
            frame_rate=sr,
            sample_width=audio.sample_width,
            channels=audio.channels
        ))

        # MFCC Çıkarımı
        mfccs = calculate_mfcc(reduced_noise, sr)
        print(f"{file_name} için MFCC şekli: {mfccs.shape}")

        # Gürültü temizlenmiş ve normalleştirilmiş ses dosyasını kaydet
        output_path = os.path.join(output_folder, file_name)
        normalized_audio.export(output_path, format="mp3")
        print(f"{file_name} dosyası gürültü temizlenmiş, normalleştirilmiş ve kaydedilmiştir.")

print("Tüm ses dosyaları başarıyla işlendi.")
