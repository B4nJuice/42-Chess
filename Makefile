OUTPUT_FILE 	= ftchess.whl
VENV			= .venv
PYTHON			= python3
V_PYTHON		= $(VENV)/bin/python3
V_PIP			= $(V_PYTHON) -m pip

DEPENDENCIES 	= build

test:
	python3 -m src.board.board

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

fclean: clean
	rm -rf $(VENV)

build: $(OUTPUT_FILE)

$(OUTPUT_FILE): $(VENV) $(SRCS)
	$(V_PIP) install $(DEPENDENCIES)
	python3 -m build -o .

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(V_PIP) install --upgrade pip