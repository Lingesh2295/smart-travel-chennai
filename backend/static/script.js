function animateBus() {
    const bus = document.getElementById("bus");
    if (!bus) return;

    bus.style.offsetDistance = "0%";
    bus.offsetHeight; // reset animation
    bus.style.offsetDistance = "100%";
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();
    if (!message) return;

    // User bubble
    const userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // Animate bus (safe)
    animateBus();

    fetch(`/chat?user_message=${encodeURIComponent(message)}`)
        .then(res => res.json())
        .then(data => {
            const botDiv = document.createElement("div");
            botDiv.className = "message bot";

            if (data.error) {
                botDiv.innerText = data.error;
            } else {
                const options = data.travel_options || {};

                botDiv.innerText =
                    `From: ${data.source}
To: ${data.destination}
Distance: ${data.distance_km} km
Time: ${data.estimated_time}

Metro: ${options.Metro?.cost || 'N/A'} • ${options.Metro?.time || 'N/A'}
Bus: ${options.Bus?.cost || 'N/A'} • ${options.Bus?.time || 'N/A'}
Auto: ${options.Auto?.cost || 'N/A'} • ${options.Auto?.time || 'N/A'}
Cab: ${options.Cab?.cost || 'N/A'} • ${options.Cab?.time || 'N/A'}`;
            }

            chatBox.appendChild(botDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(err => {
            console.error("Fetch error:", err);
        });
}
