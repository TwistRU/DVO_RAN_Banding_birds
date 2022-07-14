server <- function(input, output) {
  output$table <- DT::renderDataTable(DT::datatable(
  {
    inFile <- input$file1
    if (is.null(inFile))
      return(NULL)
    read.csv(inFile$datapath)
  },
  options = list(
          language = list(
              url = 'https://cdn.datatables.net/plug-ins/1.12.1/i18n/ru.json')
  )),
  )
}