use std::collections::{HashMap, HashSet};
use crate::sentence::Sentence;


pub struct Segmenter {
    terminals: HashSet<char>,
    parentheses: HashMap<char, char>,
    force: HashSet<char>,
    max_buf_length: usize,
}

impl Segmenter {
    pub fn new(
        terminals: Option<HashSet<char>>,
        parentheses: Option<HashMap<char, char>>,
        force: Option<HashSet<char>>,
        max_buf_length: Option<usize>,
    ) -> Self {
        let mut terminals = if let Some(ts) = terminals {
            ts
        } else {
            vec! [
                '。', '．', '，', '！', '？', '\n',
            ].into_iter().collect()
        };
        let parentheses = if let Some(ps) = parentheses {
            ps
        } else {
            vec![
                ('「', '」'),
                ('『', '』'),
                ('（', '）'),
                ('［', '］'),
                ('【', '】'),
            ].into_iter().collect()
        };
        let force = if let Some(f) = force {
            for c in f.iter() {
                terminals.insert(c.clone());
            }
            f
        } else {
            HashSet::new()
        };
        let max_buf_length = if let Some(length) = max_buf_length {
            length
        } else {
            1000
        };
        Segmenter {
            terminals,
            parentheses,
            force,
            max_buf_length,
        }
    }

    pub fn split(&self, text: String) -> Vec<Sentence> {
        let mut sentences: Vec<Sentence> = vec![];
        let mut buf: Vec<char> = vec![];
        let mut waiting_stack: Vec<char> = vec![];

        for c in text.chars() {
            buf.push(c);

            if let Some(t) = self.parentheses.get(&c) {
                waiting_stack.push(t.clone());
            } else if let Some(d) = waiting_stack.last() {
                if c == *d {
                    waiting_stack.pop();
                } else if self.force.contains(&c) {
                    sentences.push(buf.into_iter().collect());
                    buf = vec![];
                    waiting_stack.clear();
                }
            } else if self.terminals.contains(&c) {
                sentences.push(buf.into_iter().collect());
                buf = vec![];
            }

            if buf.len() >= self.max_buf_length {
                sentences.push(buf.into_iter().collect());
                buf = vec![];
                waiting_stack.clear()
            }
        }

        if buf.len() > 0 {
            sentences.push(buf.into_iter().collect());
        }

        sentences
    }
}
