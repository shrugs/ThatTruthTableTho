# ThatTruthTableTho (T4)

Generates truth-table-style Verilog ISim commands.

## Usage

    python permutate.py A B C 10
    
    >>> A = 0;
    >>> B = 0;
    >>> C = 0;
    >>> #10;
    >>> 
    >>> A = 0;
    >>> B = 0;
    >>> C = 1;
    >>> #10;
    >>> 
    >>> A = 0;
    >>> B = 1;
    >>> C = 0;
    >>> #10;
    >>> 
    >>> A = 0;
    >>> B = 1;
    >>> C = 1;
    >>> #10;
    >>> 
    >>> A = 1;
    >>> B = 0;
    >>> C = 0;
    >>> #10;
    >>> 
    >>> A = 1;
    >>> B = 0;
    >>> C = 1;
    >>> #10;
    >>> 
    >>> A = 1;
    >>> B = 1;
    >>> C = 0;
    >>> #10;
    >>> 
    >>> A = 1;
    >>> B = 1;
    >>> C = 1;
    >>> #10;

Copy/Paste that into your Verilog ISim file and you've got a nice truth table test.

## TODO

- Could use some exported comments for clarity and navigation (these things can get large with 4+ inputs).

## License

MIT, I guess.
