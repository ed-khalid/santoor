import pyaudio  
import wave 


form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1khz sample rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 4 # seconds to record 
dev_index = 0 #device index found 
wav_output_filename = 'test1.wav' # name of .wav file


audio = pyaudio.PyAudio()

# create stream
stream = audio.open(format = form_1, rate = samp_rate, channels = chans, \
                   input_device_index = dev_index, input = True, \
                   frames_per_buffer = chunk)
print("rec")
frames = []

for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished rec")

# stop stream ,close and terminate
stream.stop_stream()
stream.close()
audio.terminate()

# save as .wave
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
