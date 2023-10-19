# ProjetoTelecom
Projeto de tradutor de arquivo WAV para notas musicais

Para usar é necessário fazer pull e trocar os repositórios. O projeto utiliza o a Basic Pitch que é uma biblioteca Python para Transcrição Musical Automatica (TMA).
Para começar, devemos abrir o arquivo gravador_de_som_wav1.py e gravar 10 segundos de uma melodia cantada. Após isso começamos à transcrição

1- Com o audio em formato WAV botamos o caminho do arquivo como input do decode_wav_mid.py

2-O decode_wav_mid.py vai transformar nosso audio WAV em um arquivo formato MIDI com auxilio da biblioteca BasicPitch

3- Com o audio MIDI podemos por o input do transcritor_mid_em_notas.py, que transformará nosso audio MIDI em um output escrito das notas cantadas inicialmente
