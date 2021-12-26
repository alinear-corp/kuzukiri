use unicode_normalization::UnicodeNormalization;

pub trait Normalizer {
    fn normalize(text: String) -> String;
}

pub struct TrimNormalizer;
impl Normalizer for TrimNormalizer {
    fn normalize(text: String) -> String {
        String::from(text.trim())
    }
}

pub struct NFKCNormalizer;

impl Normalizer for NFKCNormalizer
{
    fn normalize(text: String) -> String {
        text.nfkc().collect()
    }
}

pub struct NormalizerPipeline;
impl Normalizer for NormalizerPipeline
{
    fn normalize(text: String) -> String {
        let text = NFKCNormalizer::normalize(text);
        let text = TrimNormalizer::normalize(text);
        text
    }
}