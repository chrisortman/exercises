defmodule Exercise1 do

  def prompt_for_float(prompt_text, invalid_message) do
    potential_value = IO.gets(prompt_text) |> Float.parse
    case potential_value do
      {value,_} -> value
      :error -> 
        IO.puts invalid_message
        prompt_for_float(prompt_text, invalid_message)
    end
  end

  def format_float(x) do
    [formatted|rest] = :io_lib.format("~.2f~n",[x])
    formatted
  end

  def main() do
    days_of_week = ~w(Sunday Monday Tuesday Wednesday Thursday Friday Saturday)
    total_sales =
      days_of_week
      |> Enum.map(fn(day) -> "Enter sales for #{day}: " end)
      |> Stream.map(&(prompt_for_float(&1, "Not a number")))
      |> Enum.sum
      |> format_float
    IO.puts "Total Sales: #{total_sales}"
  end

end



Exercise1.main()
