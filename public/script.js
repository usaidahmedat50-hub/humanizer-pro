const API_URL = "http://localhost:8000";

const inputText = document.getElementById('inputText');
const charCount = document.getElementById('charCount');
const outputText = document.getElementById('outputText');
const humanizeBtn = document.getElementById('humanizeBtn');
const statsRow = document.getElementById('statsRow');
const humanScore = document.getElementById('humanScore');
const pulseBar = document.querySelector('#pulseBar div');

inputText.addEventListener('input', () => {
    charCount.textContent = `${inputText.value.length} characters`;
});

humanizeBtn.addEventListener('click', async () => {
    const text = inputText.value.trim();
    if (!text) return;

    // Loading state
    humanizeBtn.disabled = true;
    humanizeBtn.innerHTML = `
        <span class="animate-spin rounded-full h-4 w-4 border-2 border-white/20 border-t-white mr-2"></span>
        <span>Humanizing...</span>
    `;
    outputText.style.opacity = '0.5';

    try {
        const response = await fetch(`${API_URL}/humanize`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        if (!response.ok) throw new Error('Humanization failed');

        const data = await response.json();

        // Update UI
        outputText.innerHTML = data.humanized_text;
        outputText.style.opacity = '1';
        
        // Show and animate stats
        statsRow.classList.remove('opacity-0', 'translate-y-2');
        humanScore.textContent = data.stats.human_score;
        pulseBar.style.width = `${Math.min(data.stats.burstiness * 10, 100)}%`;

    } catch (error) {
        console.error(error);
        outputText.innerHTML = `<span class="text-red-400">Error: ${error.message}</span>`;
    } finally {
        humanizeBtn.disabled = false;
        humanizeBtn.innerHTML = `
            <span>Antigravity</span>
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
        `;
    }
});
