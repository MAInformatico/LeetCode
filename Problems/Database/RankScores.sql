SELECT score, ranking "Rank"
FROM (SELECT id, score,
      (SELECT COUNT(score)+1 FROM (SELECT DISTINCT score FROM scores) i WHERE i.score > e.score) ranking FROM scores e) t
ORDER BY ranking;
