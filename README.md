# LLM-Powered Resume Optimizer 📄

**Privacy-First Local Resume Enhancement with AI Intelligence**

Transform your resume to perfectly match any job description using advanced local AI. Our privacy-focused tool leverages lightweight LLMs to optimize your resume content while keeping all your data secure on your local machine.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![AI Powered](https://img.shields.io/badge/AI-Local%20LLM-green.svg)
![Privacy](https://img.shields.io/badge/privacy-100%25%20Local-brightgreen.svg)
![GUI](https://img.shields.io/badge/interface-Tkinter-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🎯 Intelligent Resume Optimization
- **Job-Targeted Rewriting**: Automatically align your resume content with specific job requirements
- **Smart Segmentation**: Intelligently identifies and processes resume sections (Experience, Skills, Education)
- **Context-Aware Enhancement**: Maintains your authentic voice while optimizing for ATS systems
- **Keyword Integration**: Naturally incorporates relevant keywords from job descriptions

### 🧠 Local AI Processing
- **Lightweight LLM Integration**: Powered by efficient models like Phi-2 or Mistral-Instruct
- **llama-cpp-python Engine**: Optimized local inference with GGUF model support
- **Real-Time Processing**: Live streaming output shows optimization progress section-by-section
- **Hardware Flexible**: Runs on CPU with optional GPU acceleration

### 🖥️ User-Friendly Interface
- **Cross-Platform GUI**: Tkinter-based interface works on Windows, macOS, and Linux
- **Intuitive Workflow**: Simple paste-and-optimize process
- **Live Preview**: Watch your resume transform in real-time
- **Section Control**: Review and manage each optimized section individually

### 🛡️ Privacy & Security
- **100% Offline Operation**: No internet connection required after initial setup
- **Zero Data Sharing**: Your resume and job data never leave your device
- **No Cloud Dependencies**: Complete independence from external APIs
- **Local Model Storage**: All AI processing happens on your hardware

### ⚡ Performance Features
- **Streaming Output**: See results as they're generated
- **Efficient Processing**: Optimized for quick turnaround times
- **Memory Management**: Handles large documents without performance issues
- **Batch Section Processing**: Process multiple resume sections efficiently

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 4GB+ RAM (8GB recommended for optimal performance)
- 2GB+ free disk space (for models and dependencies)
- Modern CPU (AVX support recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xzotechx/llm-resume-optimizer.git
   cd llm-resume-optimizer
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Basic installation
   pip install llama-cpp-python pyyaml
   
   # For GPU acceleration (optional)
   # CUDA:
   pip install llama-cpp-python[cuda]
   # Metal (macOS):
   pip install llama-cpp-python[metal]
   ```

4. **Download LLM model**
   ```bash
   # Create models directory
   mkdir models
   
   # Download recommended model:
   # Llama-3.2-3B-Instruct-Q4_0.gguf (3.2GB)
   # Place in models/ directory
   ```

5. **Configure model path**
   ```yaml
   # Edit config.yaml
   llm_model_path: "models/Llama-3.2-3B-Instruct-Q4_0.gguf"
   
   # Alternative models:
   # llm_model_path: "models/phi-2.Q4_K_M.gguf"
   # llm_model_path: "models/Mistral-7B-Instruct-v0.1.Q4_K_M.gguf"
   ```

6. **Launch the application**
   ```bash
   python app.py
   ```

## 📖 Usage Guide

### Basic Workflow

1. **Prepare Your Materials**
   - Have your current resume text ready
   - Copy the target job description
   - Ensure the model is properly configured

2. **Launch and Input**
   - Run `python app.py` to start the GUI
   - Paste your resume in the left text area
   - Paste the job description in the designated field

3. **Optimize Your Resume**
   - Click "Optimize Resume" to begin processing
   - Watch as each section is analyzed and rewritten
   - Review the streaming output in real-time

4. **Review and Refine**
   - Examine each optimized section
   - Make manual adjustments if needed
   - Copy the final result for use

### Advanced Usage

**Custom Section Processing**
```python
# Example: Process specific sections only
sections_to_optimize = ['experience', 'skills', 'summary']
optimized_resume = optimizer.process_sections(resume_text, job_desc, sections_to_optimize)
```

**Model Performance Tuning**
```yaml
# config.yaml - Performance settings
model_settings:
  max_tokens: 512        # Maximum response length
  temperature: 0.7       # Creativity level (0.0-1.0)
  n_threads: 4          # CPU threads to use
  context_length: 2048   # Model context window
```

## 🏗️ Project Architecture

```
resume_optimizer/
├── app.py                     # Main Tkinter GUI application
├── config.yaml               # Model configuration and settings
├── requirements.txt           # Python dependencies
├── README.md                 # This documentation
├── 
├── core/                     # Core processing modules
│   ├── __init__.py           # Package initialization
│   ├── rewriter.py           # Resume processing and LLM logic
│   ├── segmenter.py          # Resume section identification
│   ├── optimizer.py          # Optimization algorithms
│   └── llm_client.py         # LLM interface and management
├── 
├── models/                   # LLM model files (gitignored)
│   ├── Llama-3.2-3B-Instruct-Q4_0.gguf
│   ├── phi-2.Q4_K_M.gguf
│   └── Mistral-7B-Instruct-v0.1.Q4_K_M.gguf
├── 
├── templates/               # Resume templates and examples
│   ├── template_resumes/    # Sample resume formats
│   └── job_descriptions/    # Example job postings
├── 
├── utils/                   # Utility functions
│   ├── text_processor.py    # Text cleaning and formatting
│   ├── keyword_extractor.py # Job description analysis
│   └── file_handler.py      # Document import/export
├── 
└── tests/                   # Unit tests and examples
    ├── test_rewriter.py     # Core functionality tests
    └── sample_data/         # Test resumes and job descriptions
```

## 🔧 Technical Details

### Resume Segmentation Algorithm

The application uses intelligent pattern recognition to identify resume sections:

```python
# Core segmentation logic
SECTION_PATTERNS = {
    'summary': r'(summary|profile|objective)',
    'experience': r'(experience|work|employment|career)',
    'skills': r'(skills|competencies|technical)',
    'education': r'(education|academic|qualifications)',
    'projects': r'(projects|portfolio|work samples)',
    'certifications': r'(certifications|licenses|credentials)'
}
```

### LLM Optimization Process

1. **Context Analysis**: Extracts key requirements from job description
2. **Section Mapping**: Identifies relevant resume sections for optimization
3. **Content Enhancement**: Rewrites content to match job requirements
4. **Keyword Integration**: Naturally incorporates important terms
5. **Consistency Check**: Ensures coherent voice across all sections

### Supported Model Formats

| Model | Size | Speed | Quality | Memory |
|-------|------|-------|---------|---------|
| Phi-2 Q4_K_M | 1.6GB | Fast ⚡ | Good | 2GB RAM |
| Llama-3.2-3B Q4_0 | 3.2GB | Medium | Better ⭐ | 4GB RAM |
| Mistral-7B Q4_K_M | 4.1GB | Slower | Best | 6GB RAM |

## 🛠️ Development

### Running in Development Mode

1. **Enable debug logging**
   ```bash
   export RESUME_OPTIMIZER_DEBUG=1  # Linux/macOS
   set RESUME_OPTIMIZER_DEBUG=1     # Windows
   python app.py
   ```

2. **Test individual components**
   ```bash
   # Test resume segmentation
   python -c "from core.segmenter import ResumeSegmenter; print('Segmentation OK')"
   
   # Test LLM integration
   python -c "from core.llm_client import LLMClient; print('LLM OK')"
   ```

### Adding New Features

**Custom Section Types**
```python
# Add new section patterns to segmenter.py
CUSTOM_SECTIONS = {
    'publications': r'(publications|papers|articles)',
    'awards': r'(awards|honors|recognition)',
    'languages': r'(languages|linguistic)'
}
```

**Model Integration**
```python
# Support for new model types
class CustomModelHandler:
    def __init__(self, model_path):
        self.model = load_custom_model(model_path)
    
    def optimize_section(self, text, job_desc):
        return self.model.generate(text, job_desc)
```

## 📊 Use Cases

### 🎯 Job Applications
- Tailor resumes for specific positions
- Optimize for Applicant Tracking Systems (ATS)
- Highlight relevant experience for each application
- Incorporate industry-specific keywords

### 💼 Career Transitions
- Reframe experience for new industries
- Emphasize transferable skills
- Adapt language for different sectors
- Bridge experience gaps strategically

### 🚀 Career Advancement
- Elevate accomplishments with stronger language
- Quantify achievements with impact metrics
- Align with senior-level job requirements
- Showcase leadership and growth

### 🔍 Multiple Applications
- Maintain different versions for various roles
- Quick customization for similar positions
- A/B testing different approaches
- Industry-specific optimization

## ⚙️ Configuration Options

### Performance Settings
```yaml
# config.yaml - Speed optimization
performance:
  fast_mode: true           # Reduce processing time
  max_tokens: 256          # Shorter responses
  batch_size: 1            # Process one section at a time
  
# Quality optimization
performance:
  fast_mode: false         # Higher quality output
  max_tokens: 1024         # Longer, detailed responses
  batch_size: 3            # Process multiple sections
```

### Customization Options
```yaml
# Optimization preferences
optimization:
  keyword_density: 0.8     # How aggressively to include keywords
  tone: "professional"     # professional, dynamic, conservative
  format_preservation: true # Maintain original formatting
  length_adjustment: 1.1   # Increase content by 10%
```

## 🤝 Contributing

We welcome contributions to enhance the Resume Optimizer!

### How to Contribute
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Implement your changes** with proper testing
4. **Update documentation** as needed
5. **Submit a pull request**

### Development Areas
- **UI/UX Improvements**: Enhance the Tkinter interface or add web GUI
- **Model Support**: Add support for new LLM models
- **Export Features**: PDF/DOCX import and export functionality
- **ATS Scoring**: Implement compatibility scoring system
- **Template System**: Pre-built resume templates

## 📋 Roadmap

### Phase 1: Core Enhancements
- [ ] **Document Import/Export**: PDF and DOCX file support
- [ ] **Manual Section Editing**: Pre and post-optimization editing
- [ **ATS Compatibility Scoring**: Resume optimization scoring system
- [ ] **Dark/Light Mode**: UI theme customization

### Phase 2: Advanced Features
- [ ] **Resume Templates**: Pre-built professional templates
- [ ] **Batch Processing**: Optimize multiple resumes simultaneously
- [ ] **Version Control**: Track and compare different resume versions
- [ ] **Analytics Dashboard**: Optimization success metrics

### Phase 3: Professional Features
- [ ] **Web Interface**: Browser-based GUI option
- [ ] **API Integration**: RESTful API for third-party tools
- [ ] **Team Features**: Collaborative resume optimization
- [ ] **Cloud Sync**: Optional encrypted cloud backup

## 🐛 Troubleshooting

### Common Issues

**Model Loading Errors**
```bash
# Verify model file exists and is complete
ls -la models/Llama-3.2-3B-Instruct-Q4_0.gguf

# Check model file integrity
python -c "from llama_cpp import Llama; Llama('models/your-model.gguf')"
```

**GUI Not Launching**
```bash
# Check Tkinter installation
python -c "import tkinter; print('Tkinter OK')"

# Install system dependencies (Linux)
sudo apt-get install python3-tk
```

**Poor Optimization Quality**
- Use a larger, higher-quality model (Mistral-7B instead of Phi-2)
- Increase `max_tokens` in config.yaml
- Provide more detailed job descriptions
- Adjust `temperature` setting for more creative output

**Performance Issues**
- Reduce `max_tokens` for faster processing
- Use smaller model variants (Q2_K instead of Q4_K_M)
- Increase `n_threads` to match your CPU cores
- Close other memory-intensive applications

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Meta AI** - For the Llama model architecture and training
- **Microsoft** - For the Phi-2 model
- **Mistral AI** - For the Mistral-Instruct models
- **llama.cpp** - For efficient local LLM inference
- **Python Community** - For excellent libraries and tools

---

**Built with ❤️ by [Ahmad | XZOTECHX](https://github.com/xzotechx)**

*Empowering job seekers with AI-powered resume optimization - privately and securely.*

## 📞 Support & Community

- 🐛 [Report Issues](https://github.com/xzotechx/llm-resume-optimizer/issues)
- 💬 [Join Discussions](https://github.com/xzotechx/llm-resume-optimizer/discussions)
- 📖 [Documentation Wiki](https://github.com/xzotechx/llm-resume-optimizer/wiki)
- ⭐ [Star the Project](https://github.com/xzotechx/llm-resume-optimizer)

### Quick Tips for Best Results
- **Be Specific**: Use detailed job descriptions for better optimization
- **Review Output**: Always review and refine AI-generated content
- **Test Different Models**: Try various models to find your preferred style
- **Iterate**: Run multiple optimizations with different approaches
- **Maintain Authenticity**: Ensure the optimized resume still represents you accurately
