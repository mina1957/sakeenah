import React, { useState } from 'react';
import axios from 'axios';
import { 
  Button, 
  Container, 
  Paper, 
  Typography, 
  Box,
  ThemeProvider,
  createTheme
} from '@mui/material';
import './App.css';

const theme = createTheme();

function App() {
  const [isRecording, setIsRecording] = useState(false);
  const [feedback, setFeedback] = useState(null);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioChunks, setAudioChunks] = useState([]);

  const verse = {
    text: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    translation: "In the name of Allah, the Entirely Merciful, the Especially Merciful"
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      const chunks = [];

      recorder.ondataavailable = (e) => {
        chunks.push(e.data);
      };

      recorder.onstop = async () => {
        const audioBlob = new Blob(chunks, { type: 'audio/wav' });
        await sendAudioToBackend(audioBlob);
      };

      recorder.start();
      setMediaRecorder(recorder);
      setAudioChunks(chunks);
      setIsRecording(true);
    } catch (err) {
      console.error('Error accessing microphone:', err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
      mediaRecorder.stop();
      setIsRecording(false);
    }
  };

  const sendAudioToBackend = async (audioBlob) => {
    try {
      const formData = new FormData();
      // Create a new Blob with proper MIME type
      const audioFile = new Blob([audioBlob], { type: 'audio/wav' });
      formData.append('audio', audioFile, 'recording.wav');
  
      console.log('Sending request to backend...');
  
      const response = await fetch('http://localhost:5000/recitation/submit', {
        method: 'POST',
        body: formData,
        mode: 'cors',
        headers: {
          'Accept': 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      console.log('Response from backend:', data);
      setFeedback(data);
  
    } catch (err) {
      console.error('Error details:', err);
      setFeedback({ 
        error: 'Failed to process recitation', 
        details: err.message 
      });
    }
  };
  
  return (
    <ThemeProvider theme={theme}>
      <Container maxWidth="sm">
        <Box sx={{ mt: 4 }}>
          <Paper elevation={3} sx={{ p: 4 }}>
            <Typography variant="h4" gutterBottom align="center">
              Sakeenah
            </Typography>

            <Box sx={{ mb: 4 }}>
              <Typography variant="h5" align="right" gutterBottom>
                {verse.text}
              </Typography>
              <Typography variant="body1" gutterBottom>
                {verse.translation}
              </Typography>
            </Box>

            <Box sx={{ display: 'flex', justifyContent: 'center', mb: 4 }}>
              <Button
                variant="contained"
                color={isRecording ? "error" : "primary"}
                onClick={isRecording ? stopRecording : startRecording}
              >
                {isRecording ? "Stop Recording" : "Start Recording"}
              </Button>
            </Box>

            {feedback && (
              <Box>
                <Typography variant="h6" gutterBottom>
                  Feedback:
                </Typography>
                <Typography>
                  {feedback.message}
                </Typography>
                {feedback.accuracy !== undefined && (
                  <Typography>
                    Accuracy: {(feedback.accuracy * 100).toFixed(1)}%
                  </Typography>
                )}
              </Box>
            )}
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
