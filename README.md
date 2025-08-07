# EMOS - Electronics Materials Operating System

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/logo_name_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="images/logo_name.svg">
  <img src="images/logo_name.svg" width="600" height="200" alt="EMOS - Electronics Materials Operating System">
</picture>

A modern web-based platform for electronics materials science research and analysis, featuring an intuitive interface for materials exploration, AI-powered analysis, and integrated computational tools.

## 🚀 Features

### Materials Exploration
- **Material Generation**: Generate new material compositions using AI-powered algorithms and predictive models
- **Database Extractor**: Extract and analyze specific material properties and data from integrated databases
- **Advanced Analysis Tools**: Comprehensive materials analysis and characterization tools
- **Materials Optimization**: Workflows for enhanced performance characteristics
- **Simulation & Modeling**: Tools for predicting material behavior under various conditions

### Electronics Applications
- **Device Synthesizability**: Evaluate feasibility and methods for synthesizing electronic devices
- **Interface Calculation**: Calculate and analyze interfaces between different materials
- **Electronic Property Prediction**: Optimization for semiconductor applications
- **Band Structure Calculations**: Electronic transport property analysis
- **Thermal Management**: Analysis for electronic device performance optimization
- **Reliability Assessment**: Failure analysis for electronic materials
- **Process Integration**: Workflows for electronic device manufacturing
- **Advanced Characterization**: Techniques for electronic materials evaluation

### AI Assistant
- **LLM Integration**: Built-in AI assistant for materials science queries
- **Interactive Chat**: Real-time assistance with materials research
- **Knowledge Base**: Access to comprehensive materials science information

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI/UX**: Modern responsive design with glassmorphism effects
- **Icons**: SVG graphics for scalable interface elements
- **Architecture**: Modular component-based structure

## 📁 Project Structure

```
EMOS/
├── index.html          # Main application interface
├── script.js          # Core JavaScript functionality
├── styles.css         # Application styling
├── images/            # Graphics and logos
│   ├── logo.svg       # Main EMOS logo
│   └── dark_logo.svg  # Dark theme logo variant
└── databases/         # [Work in Progress]
```

## 🎯 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Local web server (optional, for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/EMOS.git
   cd EMOS
   ```

2. **Open in browser**
   - Simply open `index.html` in your web browser, or
   - Use a local development server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   
   # Using PHP
   php -S localhost:8000
   ```

3. **Access the application**
   - Direct file: `file:///path/to/EMOS/index.html`
   - Local server: `http://localhost:8000`

## 🖥️ Usage

### Main Interface

The EMOS interface is divided into two main panels:

#### Left Panel - Controls
- **Information Units**: Configure databases, generators, and predictors
- **Features**: Access materials exploration and electronics application tools
- **LLM**: Interact with the AI assistant

#### Right Panel - Operating Area
- **Welcome Screen**: Starting point with navigation guidance
- **Feature Processing**: Input parameters, processing controls, and results display
- **Chat Interface**: AI assistant interaction area

### Workflow

1. **Select Information Units**: Choose relevant databases and computational tools
2. **Choose Feature**: Click on any feature button to access specific functionality
3. **Configure Inputs**: Set parameters for your analysis or calculation
4. **Process**: Execute the selected feature with your parameters
5. **Review Results**: Analyze outputs and export data as needed

### AI Assistant

- Click "LLM for EMOS" to open the chat interface
- Ask questions about materials science, properties, or applications
- Get contextual help and guidance for using EMOS features

## 🎨 Interface Features

- **Responsive Design**: Adapts to different screen sizes
- **Modern Aesthetics**: Glassmorphism effects and smooth animations
- **Interactive Elements**: Hover effects and visual feedback
- **Progress Tracking**: Real-time processing status indicators
- **Modal Views**: Focused interfaces for specific tasks

## 🔧 Development

### File Organization
- `index.html`: Main HTML structure and layout
- `script.js`: Application logic, event handlers, and AI responses
- `styles.css`: Complete styling including responsive design and animations

### Key JavaScript Functions
- `showFeatureView()`: Displays feature-specific interface
- `showLLMView()`: Opens AI assistant chat
- `startProcessing()`: Handles feature execution
- `sendChatMessage()`: Manages AI interactions

### Styling Architecture
- CSS Grid and Flexbox for layout
- CSS custom properties for theming
- Modular component styles
- Responsive breakpoints

## 🤝 Contributing

We welcome contributions to EMOS! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Implement your feature or fix
4. **Commit changes**: `git commit -m 'Add amazing feature'`
5. **Push to branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**: Describe your changes and their benefits

### Development Guidelines
- Follow existing code style and structure
- Test functionality across different browsers
- Ensure responsive design compatibility
- Document new features or changes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**EMOS** - Advancing electronics materials science through intelligent software solutions.
