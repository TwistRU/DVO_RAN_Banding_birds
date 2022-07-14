ui <- fluidPage(
  titlePanel("Визуализатор даннных кольцевания птиц"),
  sidebarPanel(
    fileInput("file1", "Выберите CSV файл", accept = ".csv"),
  ),
  DT::dataTableOutput("table")
)