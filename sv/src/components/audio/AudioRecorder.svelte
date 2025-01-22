<script lang="ts">
  import type { RecipeNote } from "$lib/models/recipe_note";

  export let fetchUrl: string;
  export let onAudioUploaded: (newNote: RecipeNote) => void;

  let recorder: MediaRecorder | null = null;
  let audioBlob: Blob | null = null;
  let isRecording: boolean = false;

  const startRecording = async (): Promise<void> => {
    const stream: MediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);

    const chunks: BlobPart[] = [];
    recorder.ondataavailable = (event: BlobEvent) => chunks.push(event.data);
    recorder.onstop = async () => {
      audioBlob = new Blob(chunks, { type: "audio/webm" });
      await sendAudio();
    };

    recorder.start();
    isRecording = true;
  };

  const stopRecordingAndSend = (): void => {
    if (recorder) {
      // a side effect of stopping the recorder is that
      // the onstop event will be triggered and the audio will be sent
      recorder.stop();
      isRecording = false;
    }
  };

  const sendAudio = async (): Promise<void> => {
    if (!audioBlob) return;

    const formData = new FormData();
    formData.append("audio_file", audioBlob, "recording.webm");

    const response: Response = await fetch(fetchUrl, {
      method: "POST",
      body: formData,
    });

    const newNote: RecipeNote = await response.json();
    console.log(newNote);
    onAudioUploaded(newNote);
  };
</script>

<button on:click={isRecording ? stopRecordingAndSend : startRecording}>
  {isRecording ? "Stop Recording" : "Start Recording"}
</button>
