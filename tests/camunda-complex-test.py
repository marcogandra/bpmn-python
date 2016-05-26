import unittest
import os

import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_visualizer as visualizer


class CamundaComplexTests(unittest.TestCase):
    """
    This class contains test for bpmn-python package functionality using a complex example of BPMN diagram
    created in bpmn-io (Camunda library implementation).
    """
    output_directory = "./output/test-camunda/complex/"
    example_directory = "../examples/camunda-complex-example.bpmn"
    output_file_with_di = "camunda-complex-example-output.xml"
    output_file_no_di = "camunda-complex-example-output-no-di.xml"
    output_dot_file = "camunda-complex-example"
    output_png_file = "camunda-complex-example"

    def test_loadCamundaComplexDiagram(self):
        """
        Test for importing a complex Camunda diagram example (as BPMN 2.0 XML) into inner representation
        and later exporting it to XML file
        """
        bpmn_graph = diagram.BPMNDiagramGraph()
        bpmn_graph.load_diagram_from_xml(os.path.abspath(self.example_directory))
        bpmn_graph.export_xml_file(self.output_directory, self.output_file_with_di)
        bpmn_graph.export_xml_file_no_di(self.output_directory, self.output_file_no_di)

    def test_loadCamundaComplexDiagramAndVisualize(self):
        """
        Test for importing a complex Camunda diagram example (as BPMN 2.0 XML) into inner representation
        and later exporting it to XML file. Includes test for visualization functionality.
        """
        bpmn_graph = diagram.BPMNDiagramGraph()
        bpmn_graph.load_diagram_from_xml(os.path.abspath(self.example_directory))
        visualizer.visualize_diagram(bpmn_graph)
        visualizer.bpmn_diagram_to_dot_file(bpmn_graph, self.output_directory + self.output_dot_file)
        visualizer.bpmn_diagram_to_png(bpmn_graph, self.output_directory + self.output_png_file)
        bpmn_graph.export_xml_file(self.output_directory, self.output_file_with_di)
        bpmn_graph.export_xml_file_no_di(self.output_directory, self.output_file_no_di)

if __name__ == '__main__':
    unittest.main()