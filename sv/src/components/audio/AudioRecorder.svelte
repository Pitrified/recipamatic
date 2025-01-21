<script lang="ts">
  export let fetchUrl: string;

  let recorder: MediaRecorder | null = null;
  let audioBlob: Blob | null = null;
  let isRecording: boolean = false;

  const startRecording = async (): Promise<void> => {
    const stream: MediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);

    const chunks: BlobPart[] = [];
    recorder.ondataavailable = (event: BlobEvent) => chunks.push(event.data);
    recorder.onstop = () => {
      audioBlob = new Blob(chunks, { type: "audio/webm" });
    };

    recorder.start();
    isRecording = true;
  };

  const stopRecording = (): void => {
    if (recorder) {
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

    const result = await response.json();
    console.log(result);
  };
</script>

<button on:click={isRecording ? stopRecording : startRecording}>
  {isRecording ? "Stop Recording" : "Start Recording"}
</button>
<button on:click={sendAudio} disabled={!audioBlob}>Send Audio</button>
