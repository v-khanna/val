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
        }

        .celebration-content {
            text-align: center;
            z-index: 10;
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
    </script>
</body>
</html>
"""

# Render the component - make it fill the viewport
components.html(valentine_html, height=800, scrolling=False)
