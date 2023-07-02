#[derive(Debug)]
pub struct HighScores<'a> {
    scores: &'a [u32]
}

impl<'a> HighScores<'a> {
    pub fn new(scores: &'a [u32]) -> Self {
        HighScores {
            scores
        }
    }

    pub fn scores(&self) -> &[u32] {
        self.scores
    }

    pub fn latest(&self) -> Option<u32> {
        self.scores.last().copied()
    }

    pub fn personal_best(&self) -> Option<u32> {
        self.scores.iter().max().copied()
    }

    pub fn personal_top_three(&self) -> Vec<u32> {
        let mut top_three: Vec<u32> = Vec::new();
        let mut copy: Vec<u32> = self
            .scores
            .iter()
            .map(|n| n.to_owned())
            .collect();
        
        copy.sort_unstable();

        for score in copy.iter().rev() {
            top_three.push(score.to_owned());

            if top_three.len() == 3 {
                break;
            }
        }
        
        top_three
    }
}
