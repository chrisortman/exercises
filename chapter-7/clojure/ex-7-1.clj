(use 'clojure.java.io)

(defn prompt-value [text]
  (println text)
  (read-line))

(defn parse-float [value]
  (Float/valueOf value))

;;Only works with strings
(defn try-parse-float [value]
  (try 
    (parse-float value)
    (catch NumberFormatException e nil)))

(defn prompt-for-float [text]
  (def prompt (comp try-parse-float prompt-value))
  (loop [entered (prompt text)]
    (if entered entered
      (recur (prompt text)))))

(defn -main [& args]
  (let [entered (prompt-value "Enter a value:")]
    (println "You entered: " entered)))
