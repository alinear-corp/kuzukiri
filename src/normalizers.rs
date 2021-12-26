use unicode_normalization::UnicodeNormalization;
use crate::sentence::Sentence;

pub trait Normalizer {
    fn normalize(text: Sentence) -> Sentence;
}

pub struct TrimNormalizer;
impl Normalizer for TrimNormalizer {
    fn normalize(text: Sentence) -> Sentence {
        Sentence::from(text.trim())
    }
}

pub struct NFKCNormalizer;

impl Normalizer for NFKCNormalizer
{
    fn normalize(text: Sentence) -> Sentence {
        text.nfkc().collect()
    }
}

pub struct NormalizerPipeline;
impl Normalizer for NormalizerPipeline
{
    fn normalize(text: Sentence) -> Sentence {
        let text = NFKCNormalizer::normalize(text);
        let text = TrimNormalizer::normalize(text);
        text
    }
}