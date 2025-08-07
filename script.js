// DOM elements
const operatingArea = document.getElementById('operatingArea');
const featureView = document.getElementById('featureView');
const llmView = document.getElementById('llmView');
const featureButtons = document.querySelectorAll('.feature-btn');
const llmButton = document.getElementById('llmBtn');
const closeChat = document.getElementById('closeChat');
const closeFeature = document.getElementById('closeFeature');
const chatInput = document.getElementById('chatInput');
const sendMessage = document.getElementById('sendMessage');
const chatMessages = document.getElementById('chatMessages');

// Functions
function showFeatureView(featureNumber, featureName, featureDesc) {
    // Hide other views
    operatingArea.classList.add('hidden');
    llmView.classList.add('hidden');
    
    // Show feature view
    featureView.classList.remove('hidden');
    
    // Update feature information in the view
    document.getElementById('featureTitle').textContent = featureName;
    document.getElementById('featureSubtitle').textContent = featureDesc;
    document.getElementById('currentFeature').textContent = featureName;
    document.getElementById('processingFeature').textContent = featureName;
    document.getElementById('outputFeature').textContent = featureName;
    
    // Reset processing state
    resetProcessing();
    
    // Add visual feedback to the clicked button
    featureButtons.forEach(btn => btn.style.transform = 'scale(1)');
    const clickedButton = document.querySelector(`[data-feature="${featureNumber}"]`);
    if (clickedButton) {
        clickedButton.style.transform = 'scale(0.95)';
        setTimeout(() => {
            clickedButton.style.transform = 'scale(1)';
        }, 150);
    }
}

function showLLMView() {
    // Hide other views
    operatingArea.classList.add('hidden');
    featureView.classList.add('hidden');
    
    // Show LLM view
    llmView.classList.remove('hidden');
    
    // Focus on chat input
    setTimeout(() => {
        chatInput.focus();
    }, 100);
    
    // Add visual feedback to LLM button
    llmButton.style.transform = 'scale(0.95)';
    setTimeout(() => {
        llmButton.style.transform = 'scale(1)';
    }, 150);
}

function showWelcomeView() {
    // Hide other views
    featureView.classList.add('hidden');
    llmView.classList.add('hidden');
    
    // Show operating area
    operatingArea.classList.remove('hidden');
}

// Chat functionality
function sendChatMessage() {
    const message = chatInput.value.trim();
    if (!message) return;
    
    // Add user message
    addMessage(message, 'user');
    
    // Clear input
    chatInput.value = '';
    
    // Simulate bot response
    setTimeout(() => {
        const botResponse = generateBotResponse(message);
        addMessage(botResponse, 'bot');
    }, 1000);
}

function addMessage(content, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}-message`;
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = content;
    
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function generateBotResponse(userMessage) {
    const responses = [
        "That's an interesting question about materials science! Let me help you with that.",
        "Based on your query, I can provide insights into material properties and behavior.",
        "Materials science involves understanding structure-property relationships. What specific aspect interests you?",
        "I can assist with crystallography, thermodynamics, mechanical properties, and more. What would you like to explore?",
        "Great question! In materials science, we often consider processing-structure-property-performance relationships.",
        "I'm here to help with your materials research. Could you provide more details about what you're working on?",
        "Materials engineering combines physics, chemistry, and engineering principles. What's your specific application?",
        "From nanomaterials to bulk properties, I can discuss various scales of material behavior. What interests you most?"
    ];
    
    // Simple keyword-based responses
    const lowerMessage = userMessage.toLowerCase();
    
    if (lowerMessage.includes('crystal') || lowerMessage.includes('structure')) {
        return "Crystal structures are fundamental to understanding material properties. Different crystal systems (cubic, tetragonal, orthorhombic, etc.) lead to different physical and mechanical properties.";
    } else if (lowerMessage.includes('mechanical') || lowerMessage.includes('strength')) {
        return "Mechanical properties like tensile strength, yield strength, and fracture toughness are crucial for engineering applications. These depend on microstructure, defects, and processing history.";
    } else if (lowerMessage.includes('thermal') || lowerMessage.includes('temperature')) {
        return "Thermal properties such as thermal conductivity, expansion coefficient, and specific heat are important for high-temperature applications and thermal management.";
    } else if (lowerMessage.includes('database')) {
        return "Materials databases are invaluable for research and design. They contain property data, phase diagrams, and processing information for thousands of materials.";
    } else if (lowerMessage.includes('predict') || lowerMessage.includes('model')) {
        return "Predictive modeling in materials science uses computational methods like DFT, molecular dynamics, and machine learning to predict material properties before synthesis.";
    } else {
        return responses[Math.floor(Math.random() * responses.length)];
    }
}

function startProcessing() {
    const progressFill = document.querySelector('.progress-fill');
    const processBtn = document.querySelector('.process-btn');
    const outputItems = document.querySelectorAll('.output-item span');
    
    // Disable button and show processing
    processBtn.disabled = true;
    processBtn.textContent = 'Processing...';
    
    // Animate progress bar
    progressFill.style.width = '100%';
    
    // Simulate processing time and update outputs
    setTimeout(() => {
        outputItems[0].textContent = 'Analysis complete - 98.5% accuracy';
        setTimeout(() => {
            outputItems[1].textContent = 'Material properties calculated';
            setTimeout(() => {
                outputItems[2].textContent = 'Optimization recommendations generated';
                
                // Re-enable button
                processBtn.disabled = false;
                processBtn.textContent = 'Start Processing';
                
                // Reset progress for next use
                setTimeout(() => {
                    progressFill.style.width = '0%';
                }, 1000);
            }, 800);
        }, 600);
    }, 2000);
}

function resetProcessing() {
    const progressFill = document.querySelector('.progress-fill');
    const processBtn = document.querySelector('.process-btn');
    const outputItems = document.querySelectorAll('.output-item span');
    
    // Reset progress bar
    progressFill.style.width = '0%';
    
    // Reset button
    processBtn.disabled = false;
    processBtn.textContent = 'Start Processing';
    
    // Reset outputs
    outputItems.forEach(item => {
        item.textContent = 'Pending...';
    });
}

// Initialize application
document.addEventListener('DOMContentLoaded', () => {
    // Feature button functionality - SINGLE EVENT LISTENER
    featureButtons.forEach(button => {
        button.addEventListener('click', function() {
            const featureNumber = this.getAttribute('data-feature');
            const featureName = this.getAttribute('data-feature-name');
            const featureDesc = this.getAttribute('data-feature-desc');
            
            showFeatureView(featureNumber, featureName, featureDesc);
        });
    });

    // LLM button functionality
    if (llmButton) {
        llmButton.addEventListener('click', showLLMView);
    }

    // Close feature functionality
    if (closeFeature) {
        closeFeature.addEventListener('click', showWelcomeView);
    }

    // Close chat functionality
    if (closeChat) {
        closeChat.addEventListener('click', showWelcomeView);
    }

    // Chat functionality
    if (sendMessage) {
        sendMessage.addEventListener('click', sendChatMessage);
    }
    
    if (chatInput) {
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
    }

    // Process button functionality
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('process-btn')) {
            startProcessing();
        }
    });

    // Add hover effects to sections
    const sections = document.querySelectorAll('.control-section');
    sections.forEach(section => {
        section.addEventListener('mouseenter', () => {
            section.style.transform = 'translateY(-2px)';
            section.style.transition = 'transform 0.3s ease';
        });
        
        section.addEventListener('mouseleave', () => {
            section.style.transform = 'translateY(0)';
        });
    });
    
    // Initialize with welcome view
    showWelcomeView();
});
