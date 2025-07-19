import re
from fuzzywuzzy import fuzz
from collections import Counter
import string
from typing import Dict, List


# Enhanced clean and tokenize function
def tokenize(text: str) -> List[str]:
    """Tokenize text with more comprehensive cleaning"""
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove special characters but keep some meaningful symbols like '+' (for C++)
    text = re.sub(r"[^\w\s\+#]", "", text)
    # Tokenize and remove single characters (except possibly meaningful ones like 'c')
    tokens = re.findall(r"\b[\w#\+]{2,}\b", text)
    return tokens


# Enhanced keyword extraction
def extract_keywords(text: str, top_n: int = 30, min_word_length: int = 3) -> List[str]:
    """Extract keywords with more sophisticated filtering"""
    tokens = tokenize(text)

    # Expanded common words list
    common_words = set(
        [
            "the",
            "and",
            "with",
            "for",
            "you",
            "are",
            "this",
            "that",
            "have",
            "will",
            "your",
            "our",
            "from",
            "work",
            "company",
            "team",
            "their",
            "they",
            "would",
            "should",
            "which",
            "when",
            "what",
            "where",
            "how",
            "about",
            "been",
            "also",
            "such",
            "than",
            "them",
            "those",
            "then",
            "just",
            "like",
            "other",
            "more",
            "some",
            "only",
            "into",
            "over",
            "most",
            "make",
            "many",
            "even",
            "after",
            "before",
            "while",
            "because",
            "being",
            "under",
            "through",
            "during",
            "without",
            "could",
            "might",
            "must",
            "shall",
            "both",
            "each",
            "either",
            "neither",
            "whether",
            "these",
            "there",
            "here",
            "where",
            "every",
            "any",
            "all",
            "none",
            "same",
            "different",
            "own",
            "same",
            "so",
            "too",
            "very",
            "much",
            "may",
            "can",
            "cannot",
            "able",
            "cannot",
            "need",
            "want",
            "use",
            "used",
            "using",
            "including",
            "within",
            "between",
            "among",
            "upon",
            "based",
            "according",
            "including",
            "etc",
            "eg",
            "ie",
            "via",
            "well",
            "still",
            "yet",
            "already",
            "never",
            "always",
            "often",
            "sometimes",
            "usually",
            "generally",
            "specifically",
            "particularly",
            "especially",
            "mainly",
            "primarily",
            "essentially",
            "basically",
            "actually",
            "literally",
            "virtually",
            "nearly",
            "almost",
            "quite",
            "rather",
            "somewhat",
            "enough",
            "sufficient",
            "insufficient",
            "adequate",
            "inadequate",
            "appropriate",
            "inappropriate",
            "relevant",
            "irrelevant",
            "important",
            "unimportant",
            "necessary",
            "unnecessary",
            "required",
            "optional",
            "available",
            "unavailable",
            "current",
            "previous",
            "former",
            "latter",
            "initial",
            "final",
            "next",
            "last",
            "recent",
            "past",
            "present",
            "future",
            "new",
            "old",
            "young",
            "modern",
            "ancient",
            "recent",
            "early",
            "late",
            "annual",
            "monthly",
            "weekly",
            "daily",
            "hourly",
            "yearly",
            "quarterly",
            "biannual",
            "biennial",
            "centennial",
        ]
    )

    # Filter out common words, short words, and numbers
    keywords = [
        word
        for word in tokens
        if (
            word not in common_words
            and len(word) >= min_word_length
            and not word.isdigit()
        )
    ]

    # Count frequency and get most common
    freq = Counter(keywords)

    # Filter out words that appear only once if we have enough keywords
    if len(freq) > top_n * 1.5:  # Only filter if we have plenty of candidates
        keywords = [word for word, count in freq.most_common() if count > 1]

    return [word for word, _ in freq.most_common(top_n)]


# Enhanced keyword match score with partial matches
def keyword_match(resume_text: str, jd_text: str) -> float:
    """Calculate keyword match score with partial matching"""
    resume_tokens = set(tokenize(resume_text))  # Using set for faster lookup
    jd_keywords = extract_keywords(jd_text)

    if not jd_keywords:
        return 0.0

    # Exact match score
    exact_matched = sum(1 for kw in jd_keywords if kw in resume_tokens)
    exact_score = (exact_matched / len(jd_keywords)) * 100

    # Partial/fuzzy match score (for similar but not identical terms)
    partial_match_threshold = 85  # Fuzzy match threshold
    partial_matches = 0

    for jd_kw in jd_keywords:
        if jd_kw in resume_tokens:
            continue  # Already counted in exact matches

        # Find best fuzzy match in resume
        best_ratio = max(
            [fuzz.ratio(jd_kw, resume_kw) for resume_kw in resume_tokens], default=0
        )

        if best_ratio >= partial_match_threshold:
            partial_matches += 0.5  # Partial match gets half credit

    partial_score = (partial_matches / len(jd_keywords)) * 100

    # Combine scores (70% exact, 30% partial)
    total_score = (exact_score * 0.7) + (partial_score * 0.3)

    return round(total_score, 2)


# Enhanced section detection with pattern matching
def section_match(resume_text: str) -> float:
    """Detect resume sections with more sophisticated patterns"""
    section_patterns = {
        "experience": [
            r"work\s*experience",
            r"professional\s*experience",
            r"employment\s*history",
            r"\bexperience\b",
        ],
        "education": [
            r"education",
            r"academic\s*background",
            r"degrees",
            r"qualifications",
            r"certifications",
        ],
        "skills": [
            r"technical\s*skills",
            r"key\s*skills",
            r"core\s*competencies",
            r"skills\s*summary",
            r"\bskills\b",
        ],
        "projects": [
            r"projects",
            r"personal\s*projects",
            r"academic\s*projects",
            r"selected\s*projects",
        ],
        "achievements": [r"achievements", r"accomplishments", r"awards", r"honors"],
    }

    detected_sections = 0
    resume_lower = resume_text.lower()

    for section, patterns in section_patterns.items():
        if any(re.search(pattern, resume_lower) for pattern in patterns):
            detected_sections += 1

    # Calculate percentage based on total sections we're looking for
    total_sections = len(section_patterns)
    return round((detected_sections / total_sections) * 100, 2)


# Enhanced scoring with additional metrics
def get_score(resume_text: str, jd_text: str) -> Dict[str, float]:
    """Calculate comprehensive matching scores"""
    scores = {
        "keyword_match": keyword_match(resume_text, jd_text),
        "section_match": section_match(resume_text),
        "keyword_density": 0,  # Will be calculated
        "overall_score": 0,  # Will be calculated
    }

    # Calculate keyword density (percentage of JD keywords in resume)
    jd_keywords = extract_keywords(jd_text)
    resume_tokens = tokenize(resume_text)
    total_resume_words = len(resume_tokens)

    if total_resume_words > 0 and jd_keywords:
        matched_keywords = [kw for kw in jd_keywords if kw in resume_tokens]
        keyword_density = (len(matched_keywords) / total_resume_words) * 100
        scores["keyword_density"] = round(min(keyword_density, 5), 2)  # Cap at 5%

    return scores


# Enhanced final score calculation with more factors
def calculate_final_score(
    scores: Dict[str, float], weights: Dict[str, float] = None
) -> Dict[str, float]:
    """Calculate weighted final score with normalization"""
    if weights is None:
        weights = {"keyword_match": 0.6, "section_match": 0.2, "keyword_density": 0.2}

    # Normalize weights to sum to 1
    total_weight = sum(weights.values())
    if total_weight == 0:
        weights = {k: 1 / len(weights) for k in weights}  # Equal weights if all zero
    else:
        weights = {k: v / total_weight for k, v in weights.items()}

    # Calculate weighted score
    weighted_score = sum(
        scores.get(metric, 0) * weight for metric, weight in weights.items()
    )

    # Apply sigmoid function to get score between 0-100
    def sigmoid(x):
        return 100 / (1 + 2.71828 ** (-0.1 * (x - 50)))

    overall_score = sigmoid(weighted_score)

    scores["overall_score"] = round(overall_score, 2)
    return scores
