(use 'clojure.java.io)

(defn -main [& args]

  (println "Enter a filename:")
  (let [filename (read-line)]
    (println "You entered" filename)
    (with-open [rdr (reader filename)]
      (let [lines (line-seq rdr)]
        (loop [[x & xs] lines
               counter 1]
          (println counter x)
          (recur xs (inc counter)))))))
