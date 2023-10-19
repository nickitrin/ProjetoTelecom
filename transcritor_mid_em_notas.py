import mido

# Mapeamento de números MIDI para notas musicais (escala DÓ, RE, MI na quarta oitava)
midi_to_notes = {
    36: "DÓ", 38: "RÉ", 40: "MI", 41: "FÁ", 43: "SOL", 45: "LÁ", 47: "SI", 48: "DÓ",
    50: "RÉ", 52: "MI", 53: "FÁ", 55: "SOL", 57: "LÁ", 59: "SI", 60: "DÓ",
    62: "RÉ", 64: "MI", 65: "FÁ", 67: "SOL", 69: "LÁ", 71: "SI", 72: "DÓ",
    74: "RÉ", 76: "MI", 77: "FÁ", 79: "SOL", 81: "LÁ", 83: "SI", 84: "DÓ"
}

# Carregue o arquivo MIDI
input_file = "C:\\Users\\nicol\\Downloads\\basicpitch.mid"

midi_file = mido.MidiFile(input_file)

# Percorra todas as trilhas no arquivo MIDI
for i, track in enumerate(midi_file.tracks):
    print(f"Track {i + 1}:")

    for msg in track:
        if msg.type == "note_on":
            note_name = midi_to_notes.get(msg.note, "Desconhecida")
            print(f"Tempo: {msg.time} - Nota: {note_name} - Velocidade: {msg.velocity}")

# Lembre-se de substituir "exemplo.mid" pelo nome do seu arquivo MIDI.


