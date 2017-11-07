(use 'clojure.java.io)
(defn prompt-filename []
  (println "Please enter a filename: ")
  (read-line))

(defn -main [& args]
  (with-open [rdr (reader (prompt-filename))]
    (doseq [line (line-seq rdr)]
      (println line))))


