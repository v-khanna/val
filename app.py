import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="For Rohini",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide ALL Streamlit UI and make iframe full height
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #FAF8F5;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
    .stMainBlockContainer {
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# The complete interactive Valentine component
valentine_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #FAF8F5 0%, #FFF5F7 50%, #FAF8F5 100%);
            min-height: 100vh;
        }

        .valentine-container {
            width: 100%;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        /* ========== FLOATING HEARTS BACKGROUND ========== */
        .floating-hearts {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }

        .mini-heart {
            position: absolute;
            color: #E8899E;
            opacity: 0;
            animation: floatHeart linear infinite;
            filter: blur(0.5px);
        }

        @keyframes floatHeart {
            0% {
                transform: translateY(100vh) rotate(0deg) scale(0.5);
                opacity: 0;
            }
            5% {
                opacity: 0.4;
            }
            50% {
                opacity: 0.6;
            }
            95% {
                opacity: 0.3;
            }
            100% {
                transform: translateY(-100px) rotate(360deg) scale(1);
                opacity: 0;
            }
        }

        /* Static scattered hearts */
        .static-heart {
            position: absolute;
            color: #E8899E;
            opacity: 0.15;
            pointer-events: none;
            animation: gentlePulse 4s ease-in-out infinite;
        }

        @keyframes gentlePulse {
            0%, 100% { transform: scale(1); opacity: 0.15; }
            50% { transform: scale(1.1); opacity: 0.25; }
        }

        /* ========== MUSIC TOGGLE ========== */
        .music-btn {
            position: fixed;
            top: 24px;
            right: 24px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 2px solid #E8899E;
            background: rgba(255, 255, 255, 0.95);
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 4px 15px rgba(232, 137, 158, 0.2);
        }

        .music-btn:hover {
            background: #E8899E;
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(232, 137, 158, 0.4);
        }

        .music-btn.playing {
            animation: musicPulse 2s infinite;
            background: #E8899E;
        }

        @keyframes musicPulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(232, 137, 158, 0.5); }
            50% { box-shadow: 0 0 0 15px rgba(232, 137, 158, 0); }
        }

        /* ========== SCREENS ========== */
        .screen {
            position: absolute;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.8s ease;
            z-index: 10;
        }

        .screen.active {
            opacity: 1;
            pointer-events: all;
        }

        /* ========== QUESTION SCREEN ========== */
        .question-content {
            text-align: center;
            z-index: 10;
        }

        .question-text {
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            font-weight: 600;
            color: #2D2926;
            margin-bottom: 0.8rem;
            animation: fadeInUp 1s ease-out;
            text-shadow: 0 2px 10px rgba(0,0,0,0.05);
            line-height: 1.2;
        }

        .subtext {
            font-family: 'Inter', sans-serif;
            font-size: clamp(1rem, 2vw, 1.3rem);
            color: #8B8580;
            margin-bottom: 3rem;
            animation: fadeInUp 1s ease-out 0.2s both;
            font-weight: 400;
            letter-spacing: 0.5px;
        }

        .button-container {
            display: flex;
            gap: 2rem;
            animation: fadeInUp 1s ease-out 0.4s both;
            position: relative;
            flex-wrap: wrap;
            justify-content: center;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ========== BUTTONS ========== */
        .btn {
            padding: 18px 50px;
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            border: none;
            border-radius: 60px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn-yes {
            background: linear-gradient(135deg, #E8899E 0%, #D4708A 100%);
            color: white;
            box-shadow: 0 8px 30px rgba(232, 137, 158, 0.4);
            min-width: 140px;
            transition: transform 0.4s cubic-bezier(0.25, 0.1, 0.25, 1), box-shadow 0.4s ease;
        }

        .btn-yes:hover {
            filter: brightness(1.05);
        }

        .btn-no {
            background: linear-gradient(135deg, #7B7570 0%, #5A5550 100%);
            color: white;
            box-shadow: 0 6px 20px rgba(90, 85, 80, 0.3);
            min-width: 140px;
        }

        .btn-no:hover {
            background: linear-gradient(135deg, #6B6560 0%, #4A4540 100%);
            transform: scale(1.05);
        }

        .btn-no {
            transition: transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
        }

        /* ========== TOOLTIP ========== */
        .tooltip {
            position: fixed;
            background: linear-gradient(135deg, #2D2926 0%, #1a1817 100%);
            color: #FFFFFF;
            padding: 10px 18px;
            border-radius: 12px;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            opacity: 0;
            transform: translateX(-50%) translateY(10px) scale(0.9);
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            pointer-events: none;
            z-index: 200;
            white-space: nowrap;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        .tooltip.visible {
            opacity: 1;
            transform: translateX(-50%) translateY(0) scale(1);
        }

        .tooltip::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-top: 8px solid #2D2926;
        }

        /* ========== CELEBRATION SCREEN ========== */
        #celebration-screen {
            background: linear-gradient(180deg, #FAF8F5 0%, #FFF0F3 50%, #FAF8F5 100%);
            overflow-y: auto;
            justify-content: flex-start;
            padding-top: 60px;
        }

        .celebration-content {
            text-align: center;
            z-index: 10;
            padding-bottom: 40px;
        }

        .gif-container {
            margin-bottom: 1.5rem;
            animation: celebrateFadeIn 0.8s ease-out;
        }

        .celebration-gif {
            width: 280px;
            max-width: 80vw;
            height: auto;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(232, 137, 158, 0.3);
        }

        .celebration-text {
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: clamp(3rem, 8vw, 5rem);
            font-weight: 700;
            color: #2D2926;
            margin-bottom: 0.8rem;
            animation: celebrateFadeIn 0.8s ease-out 0.3s both;
            text-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .celebration-subtext {
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: clamp(1.3rem, 4vw, 2.2rem);
            color: #E8899E;
            font-weight: 500;
            animation: celebrateFadeIn 0.8s ease-out 0.5s both;
        }

        @keyframes celebrateFadeIn {
            from {
                opacity: 0;
                transform: translateY(30px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        /* ========== GAMES SECTION ========== */
        .games-section {
            margin-top: 3rem;
            padding: 2rem;
            animation: celebrateFadeIn 0.8s ease-out 0.7s both;
        }

        .games-intro {
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: clamp(1.1rem, 2.5vw, 1.4rem);
            color: #6B6560;
            margin-bottom: 2rem;
            line-height: 1.6;
        }

        .days-count {
            color: #E8899E;
            font-weight: 600;
        }

        .game-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }

        .game-btn {
            padding: 12px 30px;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            border: 2px solid #E8899E;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: white;
            color: #E8899E;
        }

        .game-btn:hover, .game-btn.active {
            background: #E8899E;
            color: white;
        }

        .game-container {
            display: none;
            background: white;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 0 auto;
        }

        .game-container.active {
            display: block;
        }

        .game-canvas {
            border: 2px solid #E8899E;
            border-radius: 10px;
            display: block;
            margin: 0 auto;
            background: #1a1a2e;
        }

        .game-score {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            color: #2D2926;
            margin-top: 1rem;
        }

        .game-instructions {
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            color: #8B8580;
            margin-top: 0.5rem;
        }

        .game-over-text {
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: 1.5rem;
            color: #E8899E;
            margin-top: 1rem;
        }

        .restart-btn {
            margin-top: 1rem;
            padding: 10px 25px;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            background: #E8899E;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .restart-btn:hover {
            background: #D4708A;
            transform: scale(1.05);
        }

        .difficulty-container {
            margin: 1rem 0;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            color: #6B6560;
        }

        .difficulty-container label {
            display: block;
            margin-bottom: 0.5rem;
        }

        #difficulty-slider {
            width: 200px;
            height: 6px;
            -webkit-appearance: none;
            appearance: none;
            background: linear-gradient(to right, #FFB6C1, #E8899E, #D4708A);
            border-radius: 3px;
            outline: none;
        }

        #difficulty-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 18px;
            height: 18px;
            background: #E8899E;
            border-radius: 50%;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }

        #difficulty-slider::-moz-range-thumb {
            width: 18px;
            height: 18px;
            background: #E8899E;
            border-radius: 50%;
            cursor: pointer;
            border: none;
        }

        /* ========== CONFETTI CANVAS ========== */
        #confetti-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 50;
        }

        /* ========== RESPONSIVE ========== */
        @media (max-width: 600px) {
            .button-container {
                flex-direction: column;
                gap: 1.2rem;
            }
            .btn {
                padding: 16px 45px;
                font-size: 1.1rem;
            }
            .question-text {
                padding: 0 20px;
            }
        }
    </style>
</head>
<body>
    <div class="valentine-container">
        <!-- Floating hearts background -->
        <div class="floating-hearts" id="floating-hearts"></div>

        <!-- Music Toggle -->
        <button id="music-toggle" class="music-btn" title="Toggle music">
            <span id="music-icon">🔇</span>
        </button>

        <!-- Question Screen -->
        <div id="question-screen" class="screen active">
            <div class="question-content">
                <h1 class="question-text">Will you be my Valentine, Rohini?</h1>
                <p class="subtext">remember i love you</p>
                <div class="button-container">
                    <button id="yes-btn" class="btn btn-yes">Yes</button>
                    <button id="no-btn" class="btn btn-no">No</button>
                </div>
            </div>
        </div>

        <!-- Tooltip -->
        <div id="tooltip" class="tooltip"></div>

        <!-- Celebration Screen -->
        <div id="celebration-screen" class="screen">
            <canvas id="confetti-canvas"></canvas>
            <div class="celebration-content">
                <div class="gif-container">
                    <img src="https://media1.tenor.com/m/yaNqkG8o9UcAAAAC/hhgf.gif" alt="Yay!" class="celebration-gif">
                </div>
                <h1 class="celebration-text">Yay!</h1>
                <p class="celebration-subtext">Happy Valentine's Day, Rohini!</p>

                <!-- Games Section -->
                <div class="games-section">
                    <p class="games-intro">
                        But Valentine's Day is <span class="days-count" id="days-until"></span> away...<br>
                        In the meanwhile, here are some games for you! 💕
                    </p>

                    <div class="game-buttons">
                        <button class="game-btn" id="snake-btn" onclick="showGame('snake')">🐍 Snake</button>
                        <button class="game-btn" id="pong-btn" onclick="showGame('pong')">🏓 Pong</button>
                    </div>

                    <!-- Snake Game -->
                    <div class="game-container" id="snake-game">
                        <canvas id="snake-canvas" class="game-canvas" width="400" height="400"></canvas>
                        <p class="game-score">Score: <span id="snake-score">0</span></p>
                        <p class="game-instructions">Use arrow keys to move</p>
                        <p class="game-over-text" id="snake-game-over" style="display:none;">Game Over!</p>
                        <button class="restart-btn" id="snake-restart" style="display:none;" onclick="restartSnake()">Play Again</button>
                    </div>

                    <!-- Pong Game -->
                    <div class="game-container" id="pong-game">
                        <canvas id="pong-canvas" class="game-canvas" width="400" height="300"></canvas>
                        <p class="game-score">You: <span id="player-score">0</span> | Computer: <span id="computer-score">0</span></p>
                        <p class="game-instructions">Hold ↑ or ↓ arrow keys to move your paddle</p>
                        <div class="difficulty-container">
                            <label for="difficulty-slider">CPU Difficulty: <span id="difficulty-label">Medium</span></label>
                            <input type="range" id="difficulty-slider" min="1" max="5" value="3" oninput="updateDifficulty(this.value)">
                        </div>
                        <button class="restart-btn" onclick="restartPong()">Reset Game</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // ========== CONFIGURATION ==========
        const TRIGGER_DISTANCE = 150;
        const MAX_YES_SCALE = 3.0;  // Yes button grows up to 3x size
        const EVADES_TO_MAX = 50;   // Number of evades to reach max size

        const tooltipMessages = [
            "Nice try! 😏",
            "Not so fast!",
            "Are you sure? 🤔",
            "Think again!",
            "Nope! 💕",
            "The heart wants what it wants!",
            "Come on! 🥺",
            "You're making Yes stronger!",
            "That button is shy!",
            "Maybe reconsider? 💖"
        ];

        // ========== STATE ==========
        let evadeCount = 0;
        let tooltipIndex = 0;
        let audioContext = null;
        let isMusicPlaying = false;
        let hasStartedEvading = false;
        let noButtonOffset = { x: 0, y: 0 };  // Track cumulative offset
        let lastEvadeTime = 0;  // Throttle evade counting
        let currentYesScale = 1.0;  // Track current scale

        // ========== ELEMENTS ==========
        const noBtn = document.getElementById('no-btn');
        const yesBtn = document.getElementById('yes-btn');
        const tooltip = document.getElementById('tooltip');
        const questionScreen = document.getElementById('question-screen');
        const celebrationScreen = document.getElementById('celebration-screen');
        const musicToggle = document.getElementById('music-toggle');
        const musicIcon = document.getElementById('music-icon');
        const confettiCanvas = document.getElementById('confetti-canvas');

        // ========== FLOATING HEARTS BACKGROUND ==========
        function createFloatingHearts() {
            const container = document.getElementById('floating-hearts');

            // Create animated floating hearts
            const heartCount = 20;
            const heartSymbols = ['♥', '♡', '❤', '💕', '💗'];

            for (let i = 0; i < heartCount; i++) {
                const heart = document.createElement('div');
                heart.className = 'mini-heart';
                heart.textContent = heartSymbols[Math.floor(Math.random() * heartSymbols.length)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.fontSize = (Math.random() * 24 + 16) + 'px';
                heart.style.animationDuration = (Math.random() * 15 + 20) + 's';
                heart.style.animationDelay = (Math.random() * 20) + 's';
                container.appendChild(heart);
            }

            // Create static scattered hearts
            const staticCount = 15;
            for (let i = 0; i < staticCount; i++) {
                const heart = document.createElement('div');
                heart.className = 'static-heart';
                heart.textContent = heartSymbols[Math.floor(Math.random() * heartSymbols.length)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.top = Math.random() * 100 + '%';
                heart.style.fontSize = (Math.random() * 30 + 20) + 'px';
                heart.style.animationDelay = (Math.random() * 4) + 's';
                container.appendChild(heart);
            }
        }

        // ========== AUDIO SYSTEM ==========
        function initAudio() {
            if (!audioContext) {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playTone(frequency, duration, type = 'sine', volume = 0.1) {
            if (!audioContext) return;

            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();

            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);

            oscillator.frequency.value = frequency;
            oscillator.type = type;

            gainNode.gain.setValueAtTime(volume, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration);

            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + duration);
        }

        function playWhoosh() {
            if (!audioContext) return;

            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            const filter = audioContext.createBiquadFilter();

            oscillator.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(audioContext.destination);

            oscillator.type = 'sawtooth';
            oscillator.frequency.setValueAtTime(400, audioContext.currentTime);
            oscillator.frequency.exponentialRampToValueAtTime(100, audioContext.currentTime + 0.15);

            filter.type = 'lowpass';
            filter.frequency.value = 1000;

            gainNode.gain.setValueAtTime(0.04, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.15);

            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 0.15);
        }

        function playSparkle() {
            if (!audioContext) return;

            const notes = [523, 659, 784, 1047];
            notes.forEach((freq, i) => {
                setTimeout(() => playTone(freq, 0.3, 'sine', 0.08), i * 80);
            });
        }

        function playCelebration() {
            if (!audioContext) return;

            const melody = [523, 659, 784, 880, 1047];
            melody.forEach((freq, i) => {
                setTimeout(() => playTone(freq, 0.4, 'sine', 0.1), i * 120);
            });
        }

        let musicInterval = null;

        function startBackgroundMusic() {
            if (!audioContext || isMusicPlaying) return;

            isMusicPlaying = true;
            musicIcon.textContent = '🔊';
            musicToggle.classList.add('playing');

            const chords = [
                [261, 329, 392],
                [293, 369, 440],
                [349, 440, 523],
                [392, 493, 587],
            ];

            let chordIndex = 0;

            function playChord() {
                if (!isMusicPlaying) return;

                const chord = chords[chordIndex % chords.length];
                chord.forEach(freq => {
                    const osc = audioContext.createOscillator();
                    const gain = audioContext.createGain();

                    osc.connect(gain);
                    gain.connect(audioContext.destination);

                    osc.type = 'sine';
                    osc.frequency.value = freq;

                    gain.gain.setValueAtTime(0, audioContext.currentTime);
                    gain.gain.linearRampToValueAtTime(0.025, audioContext.currentTime + 0.5);
                    gain.gain.linearRampToValueAtTime(0.015, audioContext.currentTime + 2);
                    gain.gain.linearRampToValueAtTime(0, audioContext.currentTime + 3);

                    osc.start(audioContext.currentTime);
                    osc.stop(audioContext.currentTime + 3);
                });

                chordIndex++;
            }

            playChord();
            musicInterval = setInterval(playChord, 3000);
        }

        function stopBackgroundMusic() {
            isMusicPlaying = false;
            musicIcon.textContent = '🔇';
            musicToggle.classList.remove('playing');

            if (musicInterval) {
                clearInterval(musicInterval);
                musicInterval = null;
            }
        }

        musicToggle.addEventListener('click', () => {
            initAudio();
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }

            if (isMusicPlaying) {
                stopBackgroundMusic();
            } else {
                startBackgroundMusic();
            }
        });

        // ========== EVASION LOGIC ==========
        function handleCursorMove(clientX, clientY) {
            if (!questionScreen.classList.contains('active')) return;

            const rect = noBtn.getBoundingClientRect();
            const btnCenterX = rect.left + rect.width / 2;
            const btnCenterY = rect.top + rect.height / 2;

            const dx = clientX - btnCenterX;
            const dy = clientY - btnCenterY;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < TRIGGER_DISTANCE && distance > 0) {
                // Initialize audio on first evade
                if (!hasStartedEvading) {
                    hasStartedEvading = true;
                    initAudio();
                    if (audioContext && audioContext.state === 'suspended') {
                        audioContext.resume();
                    }
                }

                // Calculate escape: move away from cursor proportionally
                const escapeStrength = (TRIGGER_DISTANCE - distance) / TRIGGER_DISTANCE;
                const escapeX = -(dx / distance) * escapeStrength * 80;
                const escapeY = -(dy / distance) * escapeStrength * 80;

                // Update cumulative offset
                noButtonOffset.x += escapeX;
                noButtonOffset.y += escapeY;

                // Bound the offset so button stays on screen
                const maxOffsetX = window.innerWidth * 0.35;
                const maxOffsetY = window.innerHeight * 0.3;
                noButtonOffset.x = Math.max(-maxOffsetX, Math.min(maxOffsetX, noButtonOffset.x));
                noButtonOffset.y = Math.max(-maxOffsetY, Math.min(maxOffsetY, noButtonOffset.y));

                // Apply smooth transform
                noBtn.style.transform = `translate(${noButtonOffset.x}px, ${noButtonOffset.y}px)`;

                // Count evades (throttled to once per 200ms)
                const now = Date.now();
                if (escapeStrength > 0.3 && now - lastEvadeTime > 200) {
                    lastEvadeTime = now;
                    evadeCount++;
                    incrementYesButton();

                    // Show tooltip occasionally
                    if (evadeCount % 4 === 1) {
                        const tooltipX = btnCenterX + noButtonOffset.x;
                        const tooltipY = btnCenterY + noButtonOffset.y - rect.height / 2 - 20;
                        showTooltip(tooltipX, tooltipY);
                    }

                    playWhoosh();
                }
            }
        }

        // Mouse events
        document.addEventListener('mousemove', (e) => {
            handleCursorMove(e.clientX, e.clientY);
        });

        // Touch events for mobile
        document.addEventListener('touchmove', (e) => {
            const touch = e.touches[0];
            handleCursorMove(touch.clientX, touch.clientY);
        }, { passive: true });

        // ========== YES BUTTON GROWTH ==========
        function incrementYesButton() {
            // Scale grows from 1.0 to MAX_YES_SCALE over EVADES_TO_MAX evades
            const progress = Math.min(evadeCount / EVADES_TO_MAX, 1);
            currentYesScale = 1 + progress * (MAX_YES_SCALE - 1);

            // Glow also increases
            const glowOpacity = 0.4 + progress * 0.5;
            const glowSpread = 10 + progress * 50;
            const glowBlur = 20 + progress * 40;

            yesBtn.style.transform = `scale(${currentYesScale})`;
            yesBtn.style.boxShadow = `0 8px ${glowBlur}px ${glowSpread}px rgba(232, 137, 158, ${glowOpacity})`;
        }

        // ========== TOOLTIP ==========
        function showTooltip(x, y) {
            const message = tooltipMessages[tooltipIndex % tooltipMessages.length];
            tooltipIndex++;

            tooltip.textContent = message;
            tooltip.style.left = `${x}px`;
            tooltip.style.top = `${y}px`;
            tooltip.classList.add('visible');

            setTimeout(() => {
                tooltip.classList.remove('visible');
            }, 1500);
        }

        // ========== CELEBRATION ==========
        yesBtn.addEventListener('click', () => {
            initAudio();
            if (audioContext && audioContext.state === 'suspended') {
                audioContext.resume();
            }

            playSparkle();

            questionScreen.classList.remove('active');

            setTimeout(() => {
                celebrationScreen.classList.add('active');
                playCelebration();
                startConfetti();

                if (!isMusicPlaying) {
                    startBackgroundMusic();
                }
            }, 800);
        });

        // ========== CONFETTI ==========
        class ConfettiSystem {
            constructor(canvas) {
                this.canvas = canvas;
                this.ctx = canvas.getContext('2d');
                this.particles = [];
                this.colors = ['#E8899E', '#FFB6C1', '#FF69B4', '#FFC0CB', '#FFDAB9', '#F8A5C2', '#FF85A2'];
                this.running = false;
            }

            createParticle() {
                return {
                    x: Math.random() * this.canvas.width,
                    y: Math.random() * -this.canvas.height,
                    size: Math.random() * 12 + 6,
                    color: this.colors[Math.floor(Math.random() * this.colors.length)],
                    rotation: Math.random() * 360,
                    rotationSpeed: (Math.random() - 0.5) * 10,
                    velocityX: (Math.random() - 0.5) * 5,
                    velocityY: Math.random() * 3 + 2,
                    shape: Math.random() > 0.4 ? 'rect' : (Math.random() > 0.5 ? 'circle' : 'heart'),
                    wobble: Math.random() * 10,
                    wobbleSpeed: Math.random() * 0.12 + 0.04
                };
            }

            drawHeart(x, y, size) {
                this.ctx.beginPath();
                const topCurveHeight = size * 0.3;
                this.ctx.moveTo(x, y + topCurveHeight);
                this.ctx.bezierCurveTo(x, y, x - size / 2, y, x - size / 2, y + topCurveHeight);
                this.ctx.bezierCurveTo(x - size / 2, y + (size + topCurveHeight) / 2, x, y + (size + topCurveHeight) / 2, x, y + size);
                this.ctx.bezierCurveTo(x, y + (size + topCurveHeight) / 2, x + size / 2, y + (size + topCurveHeight) / 2, x + size / 2, y + topCurveHeight);
                this.ctx.bezierCurveTo(x + size / 2, y, x, y, x, y + topCurveHeight);
                this.ctx.fill();
            }

            start() {
                this.canvas.width = window.innerWidth;
                this.canvas.height = window.innerHeight;
                this.running = true;
                this.particles = [];

                for (let i = 0; i < 180; i++) {
                    const p = this.createParticle();
                    p.y = Math.random() * this.canvas.height * 0.6 - this.canvas.height * 0.6;
                    this.particles.push(p);
                }

                this.animate();
            }

            animate() {
                if (!this.running) return;

                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

                this.particles.forEach((p, index) => {
                    p.wobble += p.wobbleSpeed;
                    p.x += p.velocityX + Math.sin(p.wobble) * 0.8;
                    p.y += p.velocityY;
                    p.rotation += p.rotationSpeed;
                    p.velocityY += 0.025;

                    this.ctx.save();
                    this.ctx.translate(p.x, p.y);
                    this.ctx.rotate(p.rotation * Math.PI / 180);
                    this.ctx.fillStyle = p.color;

                    if (p.shape === 'circle') {
                        this.ctx.beginPath();
                        this.ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
                        this.ctx.fill();
                    } else if (p.shape === 'heart') {
                        this.drawHeart(0, 0, p.size);
                    } else {
                        this.ctx.fillRect(-p.size / 2, -p.size / 4, p.size, p.size / 2);
                    }

                    this.ctx.restore();

                    if (p.y > this.canvas.height + 50) {
                        this.particles.splice(index, 1);
                    }
                });

                if (this.particles.length < 100 && Math.random() > 0.9) {
                    this.particles.push(this.createParticle());
                }

                requestAnimationFrame(() => this.animate());
            }
        }

        const confetti = new ConfettiSystem(confettiCanvas);

        function startConfetti() {
            confetti.start();
        }

        window.addEventListener('resize', () => {
            if (confetti.running) {
                confetti.canvas.width = window.innerWidth;
                confetti.canvas.height = window.innerHeight;
            }
        });

        // Initialize
        createFloatingHearts();

        // ========== DAYS UNTIL VALENTINE'S DAY ==========
        function updateDaysUntil() {
            const now = new Date();
            const currentYear = now.getFullYear();
            let valentines = new Date(currentYear, 1, 14); // Feb 14

            // If Valentine's Day has passed this year, use next year
            if (now > valentines) {
                valentines = new Date(currentYear + 1, 1, 14);
            }

            const diffTime = valentines - now;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            const daysEl = document.getElementById('days-until');
            if (daysEl) {
                if (diffDays === 0) {
                    daysEl.textContent = "TODAY";
                } else if (diffDays === 1) {
                    daysEl.textContent = "1 day";
                } else {
                    daysEl.textContent = diffDays + " days";
                }
            }
        }
        updateDaysUntil();

        // ========== GAME SWITCHING ==========
        function showGame(game) {
            document.querySelectorAll('.game-container').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.game-btn').forEach(el => el.classList.remove('active'));

            document.getElementById(game + '-game').classList.add('active');
            document.getElementById(game + '-btn').classList.add('active');

            if (game === 'snake') {
                initSnake();
            } else if (game === 'pong') {
                initPong();
            }
        }

        // ========== SNAKE GAME ==========
        let snakeCanvas, snakeCtx;
        let snake, food, direction, nextDirection, snakeScore, snakeGameOver, snakeInterval;
        const GRID_SIZE = 20;
        const SNAKE_SPEED = 120;

        function initSnake() {
            snakeCanvas = document.getElementById('snake-canvas');
            snakeCtx = snakeCanvas.getContext('2d');

            // Reset game state
            snake = [{x: 10, y: 10}];
            direction = {x: 1, y: 0};
            nextDirection = {x: 1, y: 0};
            snakeScore = 0;
            snakeGameOver = false;

            document.getElementById('snake-score').textContent = '0';
            document.getElementById('snake-game-over').style.display = 'none';
            document.getElementById('snake-restart').style.display = 'none';

            spawnFood();

            if (snakeInterval) clearInterval(snakeInterval);
            snakeInterval = setInterval(updateSnake, SNAKE_SPEED);

            drawSnake();
        }

        function spawnFood() {
            const cols = snakeCanvas.width / GRID_SIZE;
            const rows = snakeCanvas.height / GRID_SIZE;

            do {
                food = {
                    x: Math.floor(Math.random() * cols),
                    y: Math.floor(Math.random() * rows)
                };
            } while (snake.some(seg => seg.x === food.x && seg.y === food.y));
        }

        function updateSnake() {
            if (snakeGameOver) return;

            direction = nextDirection;

            const cols = snakeCanvas.width / GRID_SIZE;
            const rows = snakeCanvas.height / GRID_SIZE;

            // Calculate new head position with wrap-around
            let newX = snake[0].x + direction.x;
            let newY = snake[0].y + direction.y;

            // Wrap around borders
            if (newX < 0) newX = cols - 1;
            if (newX >= cols) newX = 0;
            if (newY < 0) newY = rows - 1;
            if (newY >= rows) newY = 0;

            const head = { x: newX, y: newY };

            // Self collision
            if (snake.some(seg => seg.x === head.x && seg.y === head.y)) {
                endSnakeGame();
                return;
            }

            snake.unshift(head);

            // Eat food
            if (head.x === food.x && head.y === food.y) {
                snakeScore += 10;
                document.getElementById('snake-score').textContent = snakeScore;
                spawnFood();
            } else {
                snake.pop();
            }

            drawSnake();
        }

        function drawSnake() {
            snakeCtx.fillStyle = '#1a1a2e';
            snakeCtx.fillRect(0, 0, snakeCanvas.width, snakeCanvas.height);

            // Draw grid (subtle)
            snakeCtx.strokeStyle = '#252542';
            for (let i = 0; i <= snakeCanvas.width; i += GRID_SIZE) {
                snakeCtx.beginPath();
                snakeCtx.moveTo(i, 0);
                snakeCtx.lineTo(i, snakeCanvas.height);
                snakeCtx.stroke();
            }
            for (let i = 0; i <= snakeCanvas.height; i += GRID_SIZE) {
                snakeCtx.beginPath();
                snakeCtx.moveTo(0, i);
                snakeCtx.lineTo(snakeCanvas.width, i);
                snakeCtx.stroke();
            }

            // Draw food (heart)
            snakeCtx.fillStyle = '#FF6B8A';
            snakeCtx.font = '16px Arial';
            snakeCtx.fillText('❤', food.x * GRID_SIZE + 2, food.y * GRID_SIZE + 16);

            // Draw snake
            snake.forEach((seg, i) => {
                const gradient = snakeCtx.createLinearGradient(
                    seg.x * GRID_SIZE, seg.y * GRID_SIZE,
                    seg.x * GRID_SIZE + GRID_SIZE, seg.y * GRID_SIZE + GRID_SIZE
                );
                gradient.addColorStop(0, i === 0 ? '#E8899E' : '#FFB6C1');
                gradient.addColorStop(1, i === 0 ? '#D4708A' : '#E8899E');

                snakeCtx.fillStyle = gradient;
                snakeCtx.beginPath();
                snakeCtx.roundRect(
                    seg.x * GRID_SIZE + 1,
                    seg.y * GRID_SIZE + 1,
                    GRID_SIZE - 2,
                    GRID_SIZE - 2,
                    4
                );
                snakeCtx.fill();
            });
        }

        function endSnakeGame() {
            snakeGameOver = true;
            clearInterval(snakeInterval);
            document.getElementById('snake-game-over').style.display = 'block';
            document.getElementById('snake-restart').style.display = 'inline-block';
        }

        function restartSnake() {
            initSnake();
        }

        // ========== PONG GAME ==========
        let pongCanvas, pongCtx;
        let playerY, computerY, ballX, ballY, ballVX, ballVY;
        let playerScorePong, computerScorePong;
        let pongRunning = false;
        let playerMovingUp = false;
        let playerMovingDown = false;
        let computerSpeed = 3.5;  // Will be adjusted by difficulty
        const PADDLE_HEIGHT = 70;
        const PADDLE_WIDTH = 10;
        const BALL_SIZE = 10;
        const PADDLE_SPEED = 7;

        function updateDifficulty(value) {
            const labels = ['Very Easy', 'Easy', 'Medium', 'Hard', 'Impossible'];
            const speeds = [1.5, 2.5, 3.5, 5, 8];
            document.getElementById('difficulty-label').textContent = labels[value - 1];
            computerSpeed = speeds[value - 1];
        }

        function initPong() {
            pongCanvas = document.getElementById('pong-canvas');
            pongCtx = pongCanvas.getContext('2d');

            playerY = pongCanvas.height / 2 - PADDLE_HEIGHT / 2;
            computerY = pongCanvas.height / 2 - PADDLE_HEIGHT / 2;

            resetBall();

            playerScorePong = 0;
            computerScorePong = 0;
            document.getElementById('player-score').textContent = '0';
            document.getElementById('computer-score').textContent = '0';

            if (!pongRunning) {
                pongRunning = true;
                requestAnimationFrame(updatePong);
            }
        }

        function resetBall() {
            ballX = pongCanvas.width / 2;
            ballY = pongCanvas.height / 2;
            ballVX = (Math.random() > 0.5 ? 1 : -1) * 4;
            ballVY = (Math.random() - 0.5) * 6;
        }

        function updatePong() {
            if (!pongRunning) return;

            // Continuous player paddle movement
            if (playerMovingUp) {
                playerY = Math.max(0, playerY - PADDLE_SPEED);
            }
            if (playerMovingDown) {
                playerY = Math.min(pongCanvas.height - PADDLE_HEIGHT, playerY + PADDLE_SPEED);
            }

            // Move ball
            ballX += ballVX;
            ballY += ballVY;

            // Top/bottom walls
            if (ballY <= 0 || ballY >= pongCanvas.height - BALL_SIZE) {
                ballVY = -ballVY;
                ballY = Math.max(0, Math.min(pongCanvas.height - BALL_SIZE, ballY));
            }

            // Player paddle collision (left)
            if (ballX <= PADDLE_WIDTH + 15 &&
                ballY + BALL_SIZE >= playerY &&
                ballY <= playerY + PADDLE_HEIGHT &&
                ballVX < 0) {
                ballVX = -ballVX * 1.05;
                ballVY += (ballY - (playerY + PADDLE_HEIGHT / 2)) * 0.1;
                ballX = PADDLE_WIDTH + 16;
            }

            // Computer paddle collision (right)
            if (ballX >= pongCanvas.width - PADDLE_WIDTH - 15 - BALL_SIZE &&
                ballY + BALL_SIZE >= computerY &&
                ballY <= computerY + PADDLE_HEIGHT &&
                ballVX > 0) {
                ballVX = -ballVX * 1.05;
                ballVY += (ballY - (computerY + PADDLE_HEIGHT / 2)) * 0.1;
                ballX = pongCanvas.width - PADDLE_WIDTH - 16 - BALL_SIZE;
            }

            // Limit ball speed
            ballVX = Math.max(-12, Math.min(12, ballVX));
            ballVY = Math.max(-8, Math.min(8, ballVY));

            // Scoring
            if (ballX < 0) {
                computerScorePong++;
                document.getElementById('computer-score').textContent = computerScorePong;
                resetBall();
            } else if (ballX > pongCanvas.width) {
                playerScorePong++;
                document.getElementById('player-score').textContent = playerScorePong;
                resetBall();
            }

            // Computer AI (uses computerSpeed variable from difficulty)
            const computerCenter = computerY + PADDLE_HEIGHT / 2;
            const ballCenter = ballY + BALL_SIZE / 2;
            if (computerCenter < ballCenter - 10) {
                computerY += computerSpeed;
            } else if (computerCenter > ballCenter + 10) {
                computerY -= computerSpeed;
            }
            computerY = Math.max(0, Math.min(pongCanvas.height - PADDLE_HEIGHT, computerY));

            drawPong();
            requestAnimationFrame(updatePong);
        }

        function drawPong() {
            // Background
            pongCtx.fillStyle = '#1a1a2e';
            pongCtx.fillRect(0, 0, pongCanvas.width, pongCanvas.height);

            // Center line
            pongCtx.strokeStyle = '#333';
            pongCtx.setLineDash([10, 10]);
            pongCtx.beginPath();
            pongCtx.moveTo(pongCanvas.width / 2, 0);
            pongCtx.lineTo(pongCanvas.width / 2, pongCanvas.height);
            pongCtx.stroke();
            pongCtx.setLineDash([]);

            // Player paddle (pink)
            const playerGradient = pongCtx.createLinearGradient(10, playerY, 10 + PADDLE_WIDTH, playerY);
            playerGradient.addColorStop(0, '#E8899E');
            playerGradient.addColorStop(1, '#D4708A');
            pongCtx.fillStyle = playerGradient;
            pongCtx.beginPath();
            pongCtx.roundRect(10, playerY, PADDLE_WIDTH, PADDLE_HEIGHT, 5);
            pongCtx.fill();

            // Computer paddle
            const compGradient = pongCtx.createLinearGradient(
                pongCanvas.width - 20, computerY,
                pongCanvas.width - 10, computerY
            );
            compGradient.addColorStop(0, '#FFB6C1');
            compGradient.addColorStop(1, '#E8899E');
            pongCtx.fillStyle = compGradient;
            pongCtx.beginPath();
            pongCtx.roundRect(pongCanvas.width - 20, computerY, PADDLE_WIDTH, PADDLE_HEIGHT, 5);
            pongCtx.fill();

            // Ball (heart shape using emoji)
            pongCtx.fillStyle = '#FF6B8A';
            pongCtx.font = '14px Arial';
            pongCtx.fillText('💕', ballX - 2, ballY + 12);
        }

        function restartPong() {
            playerScorePong = 0;
            computerScorePong = 0;
            document.getElementById('player-score').textContent = '0';
            document.getElementById('computer-score').textContent = '0';
            resetBall();
        }

        // ========== KEYBOARD CONTROLS ==========
        document.addEventListener('keydown', (e) => {
            // Snake controls
            if (document.getElementById('snake-game').classList.contains('active')) {
                switch(e.key) {
                    case 'ArrowUp':
                    case 'w':
                    case 'W':
                        if (direction.y !== 1) nextDirection = {x: 0, y: -1};
                        e.preventDefault();
                        break;
                    case 'ArrowDown':
                    case 's':
                    case 'S':
                        if (direction.y !== -1) nextDirection = {x: 0, y: 1};
                        e.preventDefault();
                        break;
                    case 'ArrowLeft':
                    case 'a':
                    case 'A':
                        if (direction.x !== 1) nextDirection = {x: -1, y: 0};
                        e.preventDefault();
                        break;
                    case 'ArrowRight':
                    case 'd':
                    case 'D':
                        if (direction.x !== -1) nextDirection = {x: 1, y: 0};
                        e.preventDefault();
                        break;
                }
            }

            // Pong controls - keydown starts movement
            if (document.getElementById('pong-game').classList.contains('active')) {
                switch(e.key) {
                    case 'ArrowUp':
                    case 'w':
                    case 'W':
                        playerMovingUp = true;
                        e.preventDefault();
                        break;
                    case 'ArrowDown':
                    case 's':
                    case 'S':
                        playerMovingDown = true;
                        e.preventDefault();
                        break;
                }
            }
        });

        // Pong controls - keyup stops movement
        document.addEventListener('keyup', (e) => {
            if (document.getElementById('pong-game').classList.contains('active')) {
                switch(e.key) {
                    case 'ArrowUp':
                    case 'w':
                    case 'W':
                        playerMovingUp = false;
                        break;
                    case 'ArrowDown':
                    case 's':
                    case 'S':
                        playerMovingDown = false;
                        break;
                }
            }
        });
    </script>
</body>
</html>
"""

# Render the component - make it fill the viewport
components.html(valentine_html, height=800, scrolling=False)
